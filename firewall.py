import random

def random_ip():
    return f"192.168.1.{random.randint(0,20)}"

def check_rules(random_ip, firewall_rules):
    for rule_ip, action in firewall_rules.items():
        if rule_ip == random_ip:
            return action
        # return immediately stops the function and sends back a value.
    return "allow"

def main():
    firewall_rules = {
        "192.168.1.2": "block",
        "192.168.1.5": "block",
        "192.168.1.10": "block",
        "192.168.1.14": "block",
        "192.168.1.17": "block",
        "192.168.1.20": "block"
    }

    block_count = 0
    allow_count = 0

    for _ in range(20):
        random_ip_addr = random_ip()
        check_result = check_rules(random_ip_addr, firewall_rules)
        if check_result == "block":
            block_count += 1
        else:
            allow_count += 1

        print(f"IP: {random_ip_addr}, Action: {check_result}.")

    print(f"Number of IPs blocked is: {block_count}. Number of IPs allowed: {allow_count}.")

if __name__ == "__main__":
    main()