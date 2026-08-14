from __future__ import annotations

from generate_recruitment_data import fixed_text, num, random_text

ROLE_ORDER = (
    "Pretender chassis",
    "Hero Commander",
    "Commander",
    "Troop",
    "Summoned Unit",
    "Mount",
    "Shape-related Unit",
)


def role_for_unit(row: dict[str, str], data) -> str:
    unit_id = num(row, "id")
    roles: set[str] = set()
    for relation in data["acquisitions"].get(unit_id, []):
        kind = relation.get("kind")
        if kind == "Pretender":
            roles.add("Pretender chassis")
        elif kind == "Hero":
            roles.add("Hero Commander")
        elif kind in {"Recruit", "Magic Site"}:
            role = str(relation.get("role") or "")
            if role == "Commander":
                roles.add("Commander")
            elif role == "Troop":
                roles.add("Troop")
            elif role == "Summon":
                roles.add("Summoned Unit")
        elif kind == "Spell":
            if "commander" in str(relation.get("effect") or "").lower():
                roles.add("Commander")
            else:
                roles.add("Summoned Unit")
    if data["riders_by_mount"].get(unit_id):
        roles.add("Mount")
    if data["shape_outgoing"].get(unit_id) or data["shape_incoming"].get(unit_id):
        roles.add("Shape-related Unit")

    if roles:
        return " / ".join(label for label in ROLE_ORDER if label in roles)
    if fixed_text(row) != "—" or random_text(row) != "—":
        return "Magic-capable Unit record"
    return "Unit record"


def install_role_resolver(pages_module, data) -> None:
    """Replace the renderer's generic role helper with source-aware classification."""

    def resolver(row: dict[str, str]) -> str:
        return role_for_unit(row, data)

    pages_module.unit_role = resolver
