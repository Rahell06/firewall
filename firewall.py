import random


def random_ip():
    """Return a random IP address in the 192.168.1.0/24 test range."""
    return f"192.168.1.{random.randint(0, 20)}"


def check_rules(ip, firewall_rules):
    """Look up an IP in the rules and return its action.

    Returns the matching action ("block") or "allow" if no rule matches.
    """
    return firewall_rules.get(ip, "allow")


def main():
    # Rules map an IP to the action the firewall should take.
    firewall_rules = {
        "192.168.1.2": "block",
        "192.168.1.5": "block",
        "192.168.1.10": "block",
        "192.168.1.14": "block",
        "192.168.1.17": "block",
        "192.168.1.20": "block",
    }

    block_count = 0
    allow_count = 0

    # Generate a batch of IPs and run each one through the rules.
    for _ in range(20):
        ip = random_ip()
        action = check_rules(ip, firewall_rules)
        if action == "block":
            block_count += 1
        else:
            allow_count += 1

        print(f"IP: {ip}, Action: {action}.")

    print(f"Number of IPs blocked: {block_count}. Number of IPs allowed: {allow_count}.")


if __name__ == "__main__":
    main()
