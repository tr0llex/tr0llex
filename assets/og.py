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
#
# ССЫЛКА — ЭТО АДРЕС ИМЕННО ЭТОГО ПРОЕКТА, а не любой домен под рукой.
# Карточку видят в превью ссылки, отдельно от текста, который мог бы поправить:
# у deploy-kit тут стоял status.samoy.love, у metrics — samoy.love, и обе вели
# читателя не туда, куда обещал заголовок.
#
# У deploy-kit своего домена нет и не должно быть — это инструмент, а не сайт,
# поэтому в поле ссылки стоит репозиторий.
CARDS = {
    "chillhub": ("ChillHub", "A game launcher for Windows. Updates by diff.",
                 "launcher.samoy.love", "C#  ·  WPF  ·  Go"),
    "snakes": ("Snakes", "Territory capture for sixteen players.",
               "snakes.samoy.love", "Go  ·  WebSocket  ·  Canvas"),
    "metro-map": ("Metro", "The Moscow metro map, working offline.",
                  "metro.samoy.love", "React  ·  TypeScript  ·  PWA"),
    "deploy-kit": ("deploy-kit", "The shared release pipeline. Atomic, reversible.",
                   "github.com/tr0llex/deploy-kit", "Bash  ·  GitHub Actions  ·  systemd"),
    "status.samoy.love": ("status", "Uptime, versions and incidents.",
                          "status.samoy.love", "Go  ·  Astro"),
    "metrics.samoy.love": ("metrics", "Observability without a client-side tracker.",
                           "metrics.samoy.love", "Prometheus  ·  Grafana  ·  Docker"),
}

# Главная карточка профиля. Раньше она собиралась не этим скриптом и потому
# разъехалась с текстом: на ней осталось «Five services», хотя в README давно
# «пять сайтов» — сервисов и сайтов тут разное число. Один источник правды.
MAIN = ("Alexey Samoylov", "Five sites, one server, one pipeline.",
        "samoy.love  ·  alex@samoy.love", None)

out = "assets/og"
os.makedirs(out, exist_ok=True)

def card(title, sub, link, stack, owner_mark):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    x = 96
    d.rectangle([x, 168, x + 64, 172], fill=ACCENT)
    d.text((x, 212), title, font=f_name, fill=TEXT)
    d.text((x, 320), sub, font=f_sub, fill=MUTED)
    d.text((x, 424), link, font=f_mono, fill=ACCENT)
    if stack:
        d.text((x, 472), stack, font=f_mono, fill=MUTED)
    # owner mark, bottom right — на главной карточке лишний: она и так о нём
    if owner_mark:
        w = d.textlength("samoy.love", font=f_mono)
        d.text((W - 96 - w, H - 96), "samoy.love", font=f_mono, fill=MUTED)
    return img


for repo, (title, sub, link, stack) in CARDS.items():
    p = f"{out}/{repo}.png"
    card(title, sub, link, stack, owner_mark=True).save(p, "PNG")
    print(p)

card(*MAIN, owner_mark=False).save("assets/og.png", "PNG")
print("assets/og.png")
