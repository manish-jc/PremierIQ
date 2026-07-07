from app.rag.context_builder import ContextBuilder

builder = ContextBuilder()

print()

print("=" * 70)

print("PLAYER")

print("=" * 70)

print(

    builder.build_player_context(
        "Harry Kane"
    )

)

print()

print("=" * 70)

print("CLUB")

print("=" * 70)

print(

    builder.build_club_context(
        "Liverpool FC"
    )

)