# Алексей Самойлов

Русский · [English](README.en.md)

Пять сайтов, один сервер, один пайплайн. Всё ниже работает в проде на
домене `samoy.love` — он читается как фамилия — и катится одним релизным
путём, с публичной статус-страницей как доказательством.

<img src="assets/og.png" alt="Алексей Самойлов — пять сайтов, один сервер, один пайплайн" width="100%">

[alex@samoy.love](mailto:alex@samoy.love) · [samoy.love](https://samoy.love) · [t.me/tr0llex](https://t.me/tr0llex) · [status.samoy.love](https://status.samoy.love)

## Продукты

### samoy.love

[samoy.love](https://samoy.love) · [исходники](https://github.com/tr0llex/samoy.love)

Парадный вход: кто я и что тут работает. 3D-фон на WebGL, статическая сборка
отдаётся прямо из nginx, ни одного стороннего трекера.

`Astro` `TypeScript` `WebGL`

### ChillHub

[launcher.samoy.love](https://launcher.samoy.love) · [исходники](https://github.com/tr0llex/chillhub)

Лаунчер игр для Windows. Обновления по диффу: качаются только изменившиеся
файлы, целостность проверяется хешами. Своя админка и сервер раздачи сборок.

`C#` `WPF` `Go`

### Snakes

[snakes.samoy.love](https://snakes.samoy.love) · [исходники](https://github.com/tr0llex/snakes)

Захват территории на шестнадцать игроков. Бинарный протокол на 21 тип событий,
боты с полноценным ИИ, матч длится пять минут.

`Go` `WebSocket` `Canvas`

### Метро

[metro.samoy.love](https://metro.samoy.love) · [исходники](https://github.com/tr0llex/metro-map)

Схема московского метро, работает без сети. Маршруты считаются на клиенте,
раскладку схемы строит собственный решатель на Go.

`React` `TypeScript` `PWA`

## Инфраструктура

То, что делает из всего перечисленного выше одну систему, а не россыпь
пет-проектов: один релизный путь, одна статус-страница, общие контракты
`/healthz` и `/version.json`.

### deploy-kit

[исходники](https://github.com/tr0llex/deploy-kit)

Общий релизный пайплайн для всего остального. Атомарные релизы через симлинк,
автооткат по healthcheck, сверка версии после выкатки — «зелёный деплой со
старыми файлами» невозможен.

`Bash` `GitHub Actions` `systemd`

### status

[status.samoy.love](https://status.samoy.love) · [исходники](https://github.com/tr0llex/status.samoy.love)

Аптайм, версии и инциденты всех сервисов. Агент на сервере плюс внешний
сторож, который переживает падение самого хоста.

`Go` `Astro`

### metrics

[исходники](https://github.com/tr0llex/metrics.samoy.love)

Prometheus и Grafana для всего перечисленного выше, версии образов закреплены;
оба слушают localhost, снаружи — только nginx с basic auth. Посещаемость
считается из отдельного журнала nginx, в котором нет ни IP, ни User-Agent —
аналитика без клиентского трекера.

`Prometheus` `Grafana` `Docker`

---

<sub>Живые версии и аптайм: <a href="https://status.samoy.love">status.samoy.love</a></sub>
