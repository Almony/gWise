from typing import List, Optional, Dict
from features.channel.analyzer.schemas import ChannelPost


def generate_post_report(posts: List[ChannelPost]) -> str:
    """
    Generate a human-readable report from recent posts.
    """
    if not posts:
        return "Нет доступных данных для отчёта."

    top_views = sorted(posts, key=lambda p: p.views or 0, reverse=True)[:10]
    top_reacts = sorted(posts, key=lambda p: sum((p.reactions or {}).values()), reverse=True)[:10]
    weak_posts = sorted(posts, key=lambda p: (p.views or 0))[:5]

    report = "📊 *Аналитика канала:*\n\n"
    report += "🔥 *Топ 3 поста по просмотрам:*\n"
    for i, post in enumerate(top_views[:3], 1):
        report += f"{i}. 📎 ID: {post.message_id} — 👁 {post.views} просмотров\n"

    report += "\n❤️ *Топ 3 по реакциям:*\n"
    for i, post in enumerate(top_reacts[:3], 1):
        total_reacts = sum((post.reactions or {}).values())
        report += f"{i}. 📎 ID: {post.message_id} — ❤️ {total_reacts} реакций\n"

    report += "\n😓 *Наименее популярные посты:*\n"
    for i, post in enumerate(weak_posts, 1):
        report += f"{i}. 📎 ID: {post.message_id} — 👁 {post.views} просмотров\n"

    avg_views = int(sum(p.views or 0 for p in posts) / len(posts))
    report += f"\n📈 *Среднее число просмотров:* {avg_views}"

    return report


def json_report(posts: List[ChannelPost], top_n: int = 10) -> Dict:
    """
    Generate JSON-format report for AI or external analysis.
    """
    def serialize_post(p: ChannelPost) -> Dict:
        return {
            "id": p.message_id,
            "text": p.text,
            "views": p.views,
            "reactions": p.reactions,
            "forwards": p.forwards,
            "date": p.date.isoformat()
        }

    sorted_by_views = sorted(posts, key=lambda p: p.views or 0, reverse=True)
    top_posts = [serialize_post(p) for p in sorted_by_views[:top_n]]

    avg_views = int(sum(p.views or 0 for p in posts) / len(posts)) if posts else 0

    return {
        "total_posts": len(posts),
        "avg_views": avg_views,
        "top_posts": top_posts
    }
