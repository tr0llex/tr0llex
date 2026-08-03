<h1 align="center">Алексей Самойлов</h1>

<p align="center">
  Русский · <a href="README.en.md">English</a>
</p>

<p align="center">
  <b>Пять сайтов, один сервер, один пайплайн.</b><br>
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

<h2 align="center">Продукты</h2>

<table>
<tr>
<td width="50%" valign="top">

<h3><a href="https://samoy.love">samoy.love</a> <sub><a href="https://github.com/tr0llex/samoy.love">исходники</a></sub></h3>

<code>Astro</code> <code>TypeScript</code> <code>WebGL</code>

Парадный вход: кто я и что тут работает. 3D-фон на WebGL, статика прямо из
nginx, ни одного стороннего трекера.

</td>
<td width="50%" valign="top">

<h3><a href="https://launcher.samoy.love">ChillHub</a> <sub><a href="https://github.com/tr0llex/chillhub">исходники</a></sub></h3>

<code>C#</code> <code>WPF</code> <code>Go</code>

Лаунчер игр для Windows. Обновления по диффу, целостность по хешам, своя
админка и сервер раздачи сборок.

</td>
</tr>
<tr>
<td width="50%" valign="top">

<h3><a href="https://snakes.samoy.love">Snakes</a> <sub><a href="https://github.com/tr0llex/snakes">исходники</a></sub></h3>

<code>Go</code> <code>WebSocket</code> <code>Canvas</code>

Захват территории на шестнадцать игроков. Бинарный протокол на 21 тип
событий, боты с полноценным ИИ, матч на пять минут.

</td>
<td width="50%" valign="top">

<h3><a href="https://metro.samoy.love">Метро</a> <sub><a href="https://github.com/tr0llex/metro-map">исходники</a></sub></h3>

<code>React</code> <code>TypeScript</code> <code>PWA</code>

Схема московского метро без сети. Маршруты считаются на клиенте, раскладку
строит собственный решатель на Go.

</td>
</tr>
</table>

<h2 align="center">Инфраструктура</h2>

<p align="center">
  То, что делает из перечисленного выше одну систему, а не россыпь пет-проектов:<br>
  один релизный путь, одна статус-страница, общие контракты <code>/healthz</code> и <code>/version.json</code>.
</p>

<table>
<tr>
<td width="33%" valign="top">

<h3><a href="https://github.com/tr0llex/deploy-kit">deploy-kit</a></h3>

<code>Bash</code> <code>GitHub Actions</code> <code>systemd</code>

Общий релизный путь. Атомарные релизы через симлинк, откат по healthcheck
и сверка версии после выкатки.

</td>
<td width="33%" valign="top">

<h3><a href="https://status.samoy.love">status</a> <sub><a href="https://github.com/tr0llex/status.samoy.love">исходники</a></sub></h3>

<code>Go</code> <code>Astro</code>

Аптайм, версии и инциденты всех сервисов. Агент на сервере плюс внешний
сторож, который переживает падение хоста.

</td>
<td width="33%" valign="top">

<h3><a href="https://github.com/tr0llex/metrics.samoy.love">metrics</a></h3>

<code>Prometheus</code> <code>Grafana</code> <code>Docker</code>

Prometheus и Grafana на localhost, снаружи nginx с basic auth. Аналитика
из журнала, без клиентского трекера.

</td>
</tr>
</table>

<p align="center">
  <sub>Живые версии и аптайм: <a href="https://status.samoy.love">status.samoy.love</a></sub>
</p>
