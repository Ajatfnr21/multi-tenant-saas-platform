#!/usr/bin/env python3
from typing import Dict, List
from dataclasses import dataclass
from datetime import datetime
import click

@dataclass
class Tenant:
    id: str
    name: str
    domain: str
    plan: str
    is_active: bool = True

class TenantManager:
    def __init__(self):
        self.tenants: Dict[str, Tenant] = {}
        self.domains: Dict[str, str] = {}
    
    def create(self, name: str, domain: str, plan: str = "basic"):
        tid = f"t{len(self.tenants)+1}"
        tenant = Tenant(id=tid, name=name, domain=domain, plan=plan)
        self.tenants[tid] = tenant
        self.domains[domain] = tid
        return tenant
    
    def list_all(self) -> List[Tenant]:
        return list(self.tenants.values())

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.argument('domain')
@click.option('--plan', default='basic')
def create(name, domain, plan):
    mgr = TenantManager()
    t = mgr.create(name, domain, plan)
    print(f"Created: {t.name} ({t.domain}) - {t.plan}")

@cli.command()
def list():
    mgr = TenantManager()
    for t in mgr.list_all():
        print(f"{t.name}: {t.domain}")

if __name__ == "__main__":
    cli()
