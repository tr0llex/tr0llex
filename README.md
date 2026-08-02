# Alexey Samoylov

English · [Русский](README.ru.md)

Five services, one server, one pipeline. Everything below runs in production
under `samoy.love` — the domain reads as my last name — and ships through the
same release path, with a public status page as the proof.

[alex@samoy.love](mailto:alex@samoy.love) · [samoy.love](https://samoy.love) · [t.me/tr0llex](https://t.me/tr0llex) · [status.samoy.love](https://status.samoy.love)

## Products

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

Prometheus and Grafana for everything above, image versions pinned, nothing
listening beyond localhost. Traffic is counted from a separate nginx log that
records neither IP nor User-Agent — analytics without a client-side tracker.

`Prometheus` `Grafana` `Docker`

---

<sub>Live versions and uptime: <a href="https://status.samoy.love">status.samoy.love</a></sub>
