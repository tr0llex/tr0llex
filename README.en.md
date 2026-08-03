<h1 align="center">Alexey Samoylov</h1>

<p align="center">
  <a href="README.md">Русский</a> · English
</p>

<p align="center">
  <b>Five sites, one server, one pipeline.</b><br>
  Everything below runs in production under <code>samoy.love</code> — the domain reads as my last name.
</p>

<p align="center">
  <a href="https://samoy.love"><img src="https://img.shields.io/website?url=https%3A%2F%2Fsamoy.love&up_message=online&up_color=2ea043&down_message=offline&label=samoy.love" alt="prod"></a>
</p>

<p align="center">
  <a href="mailto:alex@samoy.love">alex@samoy.love</a> ·
  <a href="https://samoy.love">samoy.love</a> ·
  <a href="https://t.me/tr0llex">t.me/tr0llex</a> ·
  <a href="https://status.samoy.love">status.samoy.love</a>
</p>

<h2 align="center">Products</h2>

<table>
<tr>
<td width="50%" valign="top">

<h3><a href="https://samoy.love">samoy.love</a> <sub><a href="https://github.com/tr0llex/samoy.love">source</a></sub></h3>

<code>Astro</code> <code>TypeScript</code> <code>WebGL</code>

The front door: who I am and what runs here. A WebGL background, a static
build served straight from nginx, not a single third-party tracker.

</td>
<td width="50%" valign="top">

<h3><a href="https://launcher.samoy.love">ChillHub</a> <sub><a href="https://github.com/tr0llex/chillhub">source</a></sub></h3>

<code>C#</code> <code>WPF</code> <code>Go</code>

A game launcher for Windows. Diffed updates, hash-verified integrity, own
admin panel and build-distribution server.

</td>
</tr>
<tr>
<td width="50%" valign="top">

<h3><a href="https://snakes.samoy.love">Snakes</a> <sub><a href="https://github.com/tr0llex/snakes">source</a></sub></h3>

<code>Go</code> <code>WebSocket</code> <code>Canvas</code>

Territory capture for sixteen players. A binary protocol over 21 event types,
bots with real AI, five minutes per match.

</td>
<td width="50%" valign="top">

<h3><a href="https://metro.samoy.love">Metro</a> <sub><a href="https://github.com/tr0llex/metro-map">source</a></sub></h3>

<code>React</code> <code>TypeScript</code> <code>PWA</code>

The Moscow metro map, working offline. Routes are solved on the client, the
layout comes from a custom solver written in Go.

</td>
</tr>
</table>

<h2 align="center">Infrastructure</h2>

<p align="center">
  The part that makes all of the above one system rather than a pile of side projects:<br>
  one release path, one status page, one set of <code>/healthz</code> and <code>/version.json</code> contracts.
</p>

<table>
<tr>
<td width="33%" valign="top">

<h3><a href="https://github.com/tr0llex/deploy-kit">deploy-kit</a></h3>

<code>Bash</code> <code>GitHub Actions</code> <code>systemd</code>

The shared release path. Atomic releases via symlink, rollback on
healthcheck, version checked after.

</td>
<td width="33%" valign="top">

<h3><a href="https://status.samoy.love">status</a> <sub><a href="https://github.com/tr0llex/status.samoy.love">source</a></sub></h3>

<code>Go</code> <code>Astro</code>

Uptime, versions and incidents for every service. An agent on the server
plus an external watchdog.

</td>
<td width="33%" valign="top">

<h3><a href="https://github.com/tr0llex/metrics.samoy.love">metrics</a></h3>

<code>Prometheus</code> <code>Grafana</code> <code>Docker</code>

Prometheus and Grafana on localhost, nginx with basic auth in front.
Analytics from a log, no tracker.

</td>
</tr>
</table>

<p align="center">
  <sub>Live versions and uptime: <a href="https://status.samoy.love">status.samoy.love</a></sub>
</p>
