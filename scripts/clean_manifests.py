#!/usr/bin/env python3
import sys

# Strips resource limits & probes for resource-constrained ARM64 nodes
with open("k8s/app-manifests.yaml", "r") as f:
    lines = f.readlines()

clean = [l for l in lines if not any(k in l for k in ["livenessProbe", "readinessProbe"])]
with open("k8s/app-manifests.yaml", "w") as f:
    f.writelines(clean)
print("Manifests updated.")
