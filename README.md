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

<h3><a href="https://samoy.love">samoy.love</a></h3>

Парадный вход: кто я и что тут работает. 3D-фон на WebGL, статика прямо из
nginx, ни одного стороннего трекера.

<code>Astro</code> <code>TypeScript</code> <code>WebGL</code>

<sub><a href="https://samoy.love">сайт</a> · <a href="https://github.com/tr0llex/samoy.love">исходники</a></sub>

</td>
<td width="50%" valign="top">

<h3><a href="https://launcher.samoy.love">ChillHub</a></h3>

Лаунчер игр для Windows. Обновления по диффу, целостность по хешам, своя
админка и сервер раздачи сборок.

<code>C#</code> <code>WPF</code> <code>Go</code>

<sub><a href="https://launcher.samoy.love">сайт</a> · <a href="https://github.com/tr0llex/chillhub">исходники</a></sub>

</td>
</tr>
<tr>
<td width="50%" valign="top">

<h3><a href="https://snakes.samoy.love">Snakes</a></h3>

Захват территории на шестнадцать игроков. Бинарный протокол на 21 тип
событий, боты с полноценным ИИ, матч на пять минут.

<code>Go</code> <code>WebSocket</code> <code>Canvas</code>

<sub><a href="https://snakes.samoy.love">сайт</a> · <a href="https://github.com/tr0llex/snakes">исходники</a></sub>

</td>
<td width="50%" valign="top">

<h3><a href="https://metro.samoy.love">Метро</a></h3>

Схема московского метро без сети. Маршруты считаются на клиенте, раскладку
строит собственный решатель на Go.

<code>React</code> <code>TypeScript</code> <code>PWA</code>

<sub><a href="https://metro.samoy.love">сайт</a> · <a href="https://github.com/tr0llex/metro-map">исходники</a></sub>

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

Общий релизный путь. Атомарные релизы через симлинк, откат по healthcheck
и сверка версии после выкатки.

<code>Bash</code> <code>GitHub Actions</code> <code>systemd</code>

<sub><a href="https://github.com/tr0llex/deploy-kit">исходники</a></sub>

</td>
<td width="33%" valign="top">

<h3><a href="https://status.samoy.love">status</a></h3>

Аптайм, версии и инциденты всех сервисов. Агент на сервере плюс внешний
сторож, который переживает падение хоста.

<code>Go</code> <code>Astro</code>

<sub><a href="https://status.samoy.love">сайт</a> · <a href="https://github.com/tr0llex/status.samoy.love">исходники</a></sub>

</td>
<td width="33%" valign="top">

<h3><a href="https://github.com/tr0llex/metrics.samoy.love">metrics</a></h3>

Prometheus и Grafana на localhost, снаружи nginx с basic auth. Аналитика
из журнала, без клиентского трекера.

<code>Prometheus</code> <code>Grafana</code> <code>Docker</code>

<sub><a href="https://github.com/tr0llex/metrics.samoy.love">исходники</a></sub>

</td>
</tr>
</table>

<p align="center">
  <sub>Живые версии и аптайм: <a href="https://status.samoy.love">status.samoy.love</a></sub>
</p>
