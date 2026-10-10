# Permissions

| Action | Anonymous | Operator | Analyst | Admin |
|---|---:|---:|---:|---:|
| Health/readiness | Allow | Allow | Allow | Allow |
| Read fleet and analytics | Deny | Allow | Allow | Allow |
| Generate schedules/simulations | Deny | Allow | Allow | Allow |
| Import datasets | Deny | Deny | Allow | Allow |
| Change configuration | Deny | Deny | Deny | Allow |

The current local scaffold does not yet enforce these roles. Production
deployment must place authentication and authorization middleware in front of
the write and data endpoints before exposing them publicly.
