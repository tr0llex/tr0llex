from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1280, 640
BG = (12, 14, 19)
TEXT = (230, 232, 238)
MUTED = (138, 145, 160)
ACCENT = (52, 209, 222)

F = "C:/Windows/Fonts/"
f_name = ImageFont.truetype(F + "segoeuib.ttf", 76)
f_sub = ImageFont.truetype(F + "segoeui.ttf", 34)
f_mono = ImageFont.truetype(F + "consola.ttf", 28)

# repo -> (title, one-line, link, stack)
CARDS = {
    "chillhub": ("ChillHub", "A game launcher for Windows. Updates by diff.",
                 "launcher.samoy.love", "C#  ·  WPF  ·  Go"),
    "snakes": ("Snakes", "Territory capture for sixteen players.",
               "snakes.samoy.love", "Go  ·  WebSocket  ·  Canvas"),
    "metro-map": ("Metro", "The Moscow metro map, working offline.",
                  "metro.samoy.love", "React  ·  TypeScript  ·  PWA"),
    "deploy-kit": ("deploy-kit", "The shared release pipeline. Atomic, reversible.",
                   "status.samoy.love", "Bash  ·  GitHub Actions  ·  systemd"),
    "status.samoy.love": ("status", "Uptime, versions and incidents.",
                          "status.samoy.love", "Go  ·  Astro"),
    "metrics.samoy.love": ("metrics", "Observability without a client-side tracker.",
                           "samoy.love", "Prometheus  ·  Grafana  ·  Docker"),
}

out = "assets/og"
os.makedirs(out, exist_ok=True)

for repo, (title, sub, link, stack) in CARDS.items():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    x = 96
    d.rectangle([x, 168, x + 64, 172], fill=ACCENT)
    d.text((x, 212), title, font=f_name, fill=TEXT)
    d.text((x, 320), sub, font=f_sub, fill=MUTED)
    d.text((x, 424), link, font=f_mono, fill=ACCENT)
    d.text((x, 472), stack, font=f_mono, fill=MUTED)
    # owner mark, bottom right
    w = d.textlength("samoy.love", font=f_mono)
    d.text((W - 96 - w, H - 96), "samoy.love", font=f_mono, fill=MUTED)
    p = f"{out}/{repo}.png"
    img.save(p, "PNG")
    print(p)
