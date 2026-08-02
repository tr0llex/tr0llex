<h1 align="center">Алексей Самойлов</h1>

<p align="center">
  Русский · <a href="README.en.md">English</a>
</p>

<p align="center">
  Пять сайтов, один сервер, один пайплайн.<br>
  Всё ниже работает в проде на домене <code>samoy.love</code> — он читается как фамилия.
</p>

<p align="center">
  <a href="https://samoy.love"><img src="https://img.shields.io/website?url=https%3A%2F%2Fsamoy.love&up_message=online&up_color=2ea043&down_message=offline&label=samoy.love" alt="прод"></a>
</p>

<p align="center">
  <a href="mailto:alex@samoy.love">alex@samoy.love</a> ·
  <a href="https://samoy.love">samoy.love</a> ·
  <a href="https://t.me/tr0llex">t.me/tr0llex</a> ·
  <a href="https://status.samoy.love">status.samoy.love</a>
</p>

## Продукты

| Проект | Что это | Стек |
| --- | --- | --- |
| **[samoy.love](https://samoy.love)**<br>[исходники](https://github.com/tr0llex/samoy.love) | Парадный вход: кто я и что тут работает. 3D-фон на WebGL, статика прямо из nginx, ни одного стороннего трекера. | `Astro` `TypeScript` `WebGL` |
| **[ChillHub](https://launcher.samoy.love)**<br>[исходники](https://github.com/tr0llex/chillhub) | Лаунчер игр для Windows. Обновления по диффу, целостность по хешам, своя админка и сервер раздачи сборок. | `C#` `WPF` `Go` |
| **[Snakes](https://snakes.samoy.love)**<br>[исходники](https://github.com/tr0llex/snakes) | Захват территории на шестнадцать игроков. Бинарный протокол на 21 тип событий, боты с полноценным ИИ, матч на пять минут. | `Go` `WebSocket` `Canvas` |
| **[Метро](https://metro.samoy.love)**<br>[исходники](https://github.com/tr0llex/metro-map) | Схема московского метро без сети. Маршруты считаются на клиенте, раскладку строит собственный решатель на Go. | `React` `TypeScript` `PWA` |

## Инфраструктура

То, что делает из перечисленного выше одну систему, а не россыпь пет-проектов:
один релизный путь, одна статус-страница, общие контракты `/healthz` и
`/version.json`.

| Проект | Что это | Стек |
| --- | --- | --- |
| **[deploy-kit](https://github.com/tr0llex/deploy-kit)** | Общий релизный пайплайн. Атомарные релизы через симлинк, автооткат по healthcheck, сверка версии после выкатки — «зелёный деплой со старыми файлами» невозможен. | `Bash` `GitHub Actions` `systemd` |
| **[status](https://status.samoy.love)**<br>[исходники](https://github.com/tr0llex/status.samoy.love) | Аптайм, версии и инциденты всех сервисов. Агент на сервере плюс внешний сторож, который переживает падение хоста. | `Go` `Astro` |
| **[metrics](https://github.com/tr0llex/metrics.samoy.love)** | Prometheus и Grafana, оба на localhost, снаружи — nginx с basic auth. Посещаемость считается из журнала без IP и User-Agent: аналитика без клиентского трекера. | `Prometheus` `Grafana` `Docker` |

---

<p align="center">
  <sub>Живые версии и аптайм: <a href="https://status.samoy.love">status.samoy.love</a></sub>
</p>
