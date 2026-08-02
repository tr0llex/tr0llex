# Alexey Samoylov

[Русский](README.md) · English
[![CI](https://github.com/tr0llex/tr0llex/actions/workflows/ci.yml/badge.svg)](https://github.com/tr0llex/tr0llex/actions/workflows/ci.yml)
[![prod](https://img.shields.io/website?url=https%3A%2F%2Fsamoy.love&up_message=online&up_color=2ea043&down_message=offline&label=samoy.love)](https://samoy.love)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Five sites, one server, one pipeline. Everything below runs in production
under `samoy.love` — the domain reads as my last name — and ships through the
same release path, with a public status page as the proof.

<img src="assets/og.png" alt="Alexey Samoylov — five sites, one server, one pipeline" width="100%">

[alex@samoy.love](mailto:alex@samoy.love) · [samoy.love](https://samoy.love) · [t.me/tr0llex](https://t.me/tr0llex) · [status.samoy.love](https://status.samoy.love)

## Products

### samoy.love

[samoy.love](https://samoy.love) · [source](https://github.com/tr0llex/samoy.love)

The front door: who I am and what runs here. A WebGL background, a static
build served straight from nginx, not a single third-party tracker.

`Astro` `TypeScript` `WebGL`

### ChillHub

[launcher.samoy.love](https://launcher.samoy.love) · [source](https://github.com/tr0llex/chillhub)

A game launcher for Windows. Updates are diffed — only changed files travel,
integrity is verified by hash. Own admin panel and build-distribution server.

`C#` `WPF` `Go`

### Snakes

[snakes.samoy.love](https://snakes.samoy.love) · [source](https://github.com/tr0llex/snakes)

Territory capture for sixteen players. A binary protocol over 21 event types,
bots with real AI, five minutes per match.

`Go` `WebSocket` `Canvas`

### Metro

[metro.samoy.love](https://metro.samoy.love) · [source](https://github.com/tr0llex/metro-map)

The Moscow metro map, working offline. Routes are solved on the client; the
map layout is produced by a custom solver written in Go.

`React` `TypeScript` `PWA`

## Infrastructure

The part that makes all of the above one system rather than a pile of side
projects: one release path, one status page, one set of `/healthz` and
`/version.json` contracts.

### deploy-kit

[source](https://github.com/tr0llex/deploy-kit)

The shared release pipeline for everything above. Atomic releases via symlink,
automatic rollback on healthcheck, version verified after the switch — a green
deploy serving old files is not possible.

`Bash` `GitHub Actions` `systemd`

### status

[status.samoy.love](https://status.samoy.love) · [source](https://github.com/tr0llex/status.samoy.love)

Uptime, versions and incidents for every service. An agent on the server plus
an external watchdog that outlives the host going down.

`Go` `Astro`

### metrics

[source](https://github.com/tr0llex/metrics.samoy.love)

Prometheus and Grafana for everything above, image versions pinned; both bind
to localhost and the only way in is nginx with basic auth. Traffic is counted
from a separate nginx log that records neither IP nor User-Agent — analytics
without a client-side tracker.

`Prometheus` `Grafana` `Docker`

---

<sub>Live versions and uptime: <a href="https://status.samoy.love">status.samoy.love</a></sub>
