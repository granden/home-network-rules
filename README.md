# Home network rules for Shadowrocket

Subscription: https://raw.githubusercontent.com/granden/home-network-rules/main/home-network.conf

Import in Shadowrocket under Configuration → Add Configuration; select this configuration and use Config routing. Continue using your own existing node subscriptions. Enable configuration automatic updates in Shadowrocket settings (iOS background restrictions can delay them).

The configuration follows the router's general routing order as captured on 2026-11-01: domestic domains and iCloud direct, Apple Private Relay's existing proxy policy retained, upstream ad blocking and other service classifications preserved. PROXY means the node selected in Shadowrocket; it is not the router's particular node. It contains no node credentials, private subscription URLs, router addresses or device identifiers.

Sources are Sukka, DustinWin and MetaCubeX. Most lists are fetched directly from their maintained, compatible format endpoints. `update_cn.py` only converts DustinWin's exact/suffix domain format to RULE-SET format. GitHub Actions updates this one file every 12 hours, subject to GitHub scheduling and repository activity limits. If upstream fetch or validation fails, the prior file remains unchanged. The other sources update when Shadowrocket refreshes its configuration/rules.

This is a policy snapshot, not a live router connection: future custom routing edits on the router must also be reflected here. Xbox-specific interception/download acceleration is router-only. Unreferenced router providers and router DNS internals are not imported. Apple and domestic services can use different CDN endpoints on different networks, so equal routing policy does not guarantee equal speed.

Upstream: https://github.com/SukkaW/Surge (AGPL-3.0), https://github.com/DustinWin/ruleset_geodata, https://github.com/MetaCubeX/meta-rules-dat. Refer to each upstream repository for its applicable licenses. The small format-conversion script and configuration glue in this repository are provided under MIT; upstream data remains subject to upstream terms.
