<h1 align="center">Alexey Samoylov</h1>

<p align="center">
  <a href="README.md">Русский</a> · English
</p>

<p align="center">
  Five sites, one server, one pipeline.<br>
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

## Products

| Project | What it is | Stack |
| --- | --- | --- |
| **[samoy.love](https://samoy.love)**<br>[source](https://github.com/tr0llex/samoy.love) | The front door: who I am and what runs here. A WebGL background, static build served straight from nginx, not a single third-party tracker. | `Astro` `TypeScript` `WebGL` |
| **[ChillHub](https://launcher.samoy.love)**<br>[source](https://github.com/tr0llex/chillhub) | A game launcher for Windows. Diffed updates, hash-verified integrity, own admin panel and build-distribution server. | `C#` `WPF` `Go` |
| **[Snakes](https://snakes.samoy.love)**<br>[source](https://github.com/tr0llex/snakes) | Territory capture for sixteen players. A binary protocol over 21 event types, bots with real AI, five minutes per match. | `Go` `WebSocket` `Canvas` |
| **[Metro](https://metro.samoy.love)**<br>[source](https://github.com/tr0llex/metro-map) | The Moscow metro map, working offline. Routes are solved on the client; the layout comes from a custom solver written in Go. | `React` `TypeScript` `PWA` |

## Infrastructure

The part that makes all of the above one system rather than a pile of side
projects: one release path, one status page, one set of `/healthz` and
`/version.json` contracts.

| Project | What it is | Stack |
| --- | --- | --- |
| **[deploy-kit](https://github.com/tr0llex/deploy-kit)** | The shared release pipeline. Atomic releases via symlink, automatic rollback on healthcheck, version verified after the switch — a green deploy serving old files is not possible. | `Bash` `GitHub Actions` `systemd` |
| **[status](https://status.samoy.love)**<br>[source](https://github.com/tr0llex/status.samoy.love) | Uptime, versions and incidents for every service. An agent on the server plus an external watchdog that outlives the host going down. | `Go` `Astro` |
| **[metrics](https://github.com/tr0llex/metrics.samoy.love)** | Prometheus and Grafana, both bound to localhost, the only way in is nginx with basic auth. Traffic is counted from a log with neither IP nor User-Agent: analytics without a client-side tracker. | `Prometheus` `Grafana` `Docker` |

---

<p align="center">
  <sub>Live versions and uptime: <a href="https://status.samoy.love">status.samoy.love</a></sub>
</p>
