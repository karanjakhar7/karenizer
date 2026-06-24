import litellm
from app.config import LITELLM_MODEL

SYSTEM_PROMPTS: dict[int, str] = {
    0: (
        "You write calm, professional complaint letters on behalf of customers. "
        "Be polite, factual, and constructive. Use one to two concise paragraphs. "
        "Avoid drama or threats. Express disappointment clearly but respectfully."
    ),
    1: (
        "You write mildly frustrated complaint letters on behalf of customers. "
        "Show genuine disappointment and hint at reconsidering the business relationship. "
        "Use phrases like 'I am quite disappointed' and 'I expected better service.' "
        "Two paragraphs. Slightly passive-aggressive but still professional."
    ),
    2: (
        "You write noticeably annoyed complaint letters on behalf of customers. "
        "Express clear frustration using phrases like 'completely unacceptable' and "
        "'I find this highly disappointing.' Mention you are considering leaving a negative review. "
        "Two to three paragraphs. Make the reader slightly uncomfortable."
    ),
    3: (
        "You write full Karen-mode complaint letters on behalf of customers. "
        "DEMAND to speak to the manager. Use CAPS to emphasize key grievances. "
        "Mention you are a loyal customer who deserves better. "
        "Threaten negative reviews on Yelp, Google, and social media. "
        "Reference your rights as a consumer. Three paragraphs of righteous indignation."
    ),
    4: (
        "You write over-the-top, nuclear Karen complaint letters on behalf of customers. "
        "Make dramatic demands. Threaten lawyers, the Better Business Bureau, local news, "
        "and community Facebook groups. State that this affects not just you but your entire "
        "family's decision to ever return. Demand compensation. Use rhetorical questions to "
        "emphasize injustice. Three to four paragraphs. This is absolute WAR."
    ),
    5: (
        "You write MAXIMUM KAREN complaint letters — the nuclear option, the stuff of legend. "
        "Address the CEO directly. Use ALL CAPS for entire sentences of demands. "
        "Threaten to contact local news, national media, your congressman, the BBB, every major "
        "review platform, AND your neighborhood Facebook group with thousands of members. "
        "Demand a full refund, compensation for emotional distress, a personal written apology "
        "from the CEO, and permanent policy changes. Reference the severity in near-biblical terms. "
        "Invoke the spirit of every wronged customer in history. "
        "Four to five paragraphs of pure, concentrated, legendary Karen energy."
    ),
}


async def generate_karen_complaint(
    company_name: str,
    complaint_body: str,
    complaint_type: str,
    karen_level: int,
) -> str:
    type_display = complaint_type.replace("_", " ").title()
    user_prompt = (
        f"Write a complaint letter to {company_name} about the following "
        f"{type_display} issue:\n\n{complaint_body}\n\n"
        "Requirements:\n"
        "- Write in first person as the customer\n"
        f'- Address the letter to "{company_name}"\n'
        '- Sign it as "A Concerned Customer"\n'
        "- Start directly with the greeting (no subject line, headers, or RE: prefix)\n"
        "- Be specific about the exact issue described above"
    )

    response = await litellm.acompletion(
        model=LITELLM_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPTS[karen_level]},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.85,
        max_tokens=1200,
    )

    return response.choices[0].message.content
