# Example: XSIAM API Returns Forbidden

## Objective

Diagnose a reported forbidden response without exposing credentials or granting broad administrator access.

## Target and evidence

- Claimed product: Cortex XSIAM Platform API.
- Endpoint, version, tenant FQDN, operation, response body, identity, role, and scope: `Unknown`.
- Status: `UNVERIFIED / TENANT-UNVERIFIED`.

## Authorization layers

Authentication and authorization are different. Inspect:

1. tenant API FQDN and current endpoint family;
2. API key/key-ID pairing without printing values;
3. feature/license availability;
4. component-level RBAC;
5. dataset permission;
6. SBAC row/entity scope;
7. object sharing where applicable;
8. integration-command permission where applicable;
9. external-system privilege for a proxied integration command.

Sources: [Get started with Cortex XSIAM APIs](https://cortex-docs.paloaltonetworks.com/xsiam-api/get-started-with-cortex-apis.md), [Manage user access](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Manage-user-access), and [Configure integration permissions](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-3.x-Documentation/Configure-integration-permissions).

## Discriminating checks

- Confirm the endpoint from the current API index; do not reconstruct it from memory.
- Record only response status/class, correlation ID, time, and sanitized error.
- Compare effective accumulated permissions against the operation.
- Test one documented harmless read that the identity is intended to perform.
- If the operation targets data, test positive and negative scope with approved identities.
- If it is a command, inspect the exact instance/command role restriction.

## Safety

Do not paste a key into chat, source, or logs. Do not assign an administrator role as a diagnostic shortcut. Request the smallest missing permission/scope with owner approval and retest the negative boundary.

## Validation

No API request was made in this example. The cause remains unverified; C/E are `NOT RUN`.

