# Firewall Simulation

A small Python script that simulates the core idea behind a firewall: checking IP
addresses against a rule set and deciding whether to **block** or **allow** each one.
This was my first script — I keep it here as a learning artifact.

## What it does

- Defines a rule set that maps specific IP addresses to a `block` action.
- Generates 20 random IPs in the `192.168.1.0/24` range.
- Checks each IP against the rules and prints whether it was blocked or allowed.
- Prints a final tally of blocked vs. allowed IPs.

## How it works

- `random_ip()` produces a random address in `192.168.1.0` – `192.168.1.20`.
- `check_rules(ip, firewall_rules)` looks the IP up in the rules dictionary and
  returns its action, defaulting to `allow` when no rule matches (a default-allow policy).
- `main()` runs 20 iterations, counts the results, and prints the summary.

## Requirements

- Python 3 (standard library only — no external packages).

## Usage

```bash
python3 firewall.py
```

Example output:

```
IP: 192.168.1.7, Action: allow.
IP: 192.168.1.10, Action: block.
...
Number of IPs blocked: 6. Number of IPs allowed: 14.
```

## Limitations

This is an educational simulation, not a real firewall:

- IPs are random rather than read from live traffic.
- Matching is exact-IP only — no CIDR ranges, ports, protocols, or directions.
- The policy is static and default-allow; there is no logging or persistence.
- It does not interact with the network or the OS packet filter in any way.
