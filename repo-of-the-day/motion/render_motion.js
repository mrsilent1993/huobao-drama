// Dựng hình động từ engine.html: node render_motion.js data.json out_silent.mp4
// Mỗi khung hình gọi setTime(t) rồi chụp màn hình, đẩy thẳng vào ffmpeg (30 khung/giây, 1080x1920).
const { chromium } = require("playwright");
const { spawn } = require("child_process");
const fs = require("fs");
const path = require("path");

(async () => {
  const [dataPath, out] = process.argv.slice(2);
  const data = JSON.parse(fs.readFileSync(dataPath, "utf8"));
  const fps = 30, frames = Math.ceil(data.total * fps);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await page.addInitScript(d => { window.DATA = d; }, data);
  await page.goto("file://" + path.join(__dirname, "engine.html"));
  await page.waitForFunction(() => window.READY === true);
  await page.evaluate(() => document.fonts.ready);
  const ff = spawn("ffmpeg", ["-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(fps), "-i", "-",
    "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", out], { stdio: ["pipe", "inherit", "inherit"] });
  for (let f = 0; f < frames; f++) {
    await page.evaluate(t => window.setTime(t), f / fps);
    const buf = await page.screenshot({ type: "jpeg", quality: 92 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once("drain", r));
  }
  ff.stdin.end();
  await new Promise(r => ff.on("close", r));
  await browser.close();
  console.log("motion ok", frames, "frames");
})();
