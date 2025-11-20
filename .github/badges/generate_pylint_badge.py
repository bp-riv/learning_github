"""
This is a standard script, available online, to generate a .svg badge file
reading the content of coverage.json.
This script is supposed to be run from the repository root directory,
so that the script is located in .github/badges,
where the output files will also be located.
"""
import json
import os
import datetime

comment = "Generated at time: "
comment = comment + str(datetime.datetime.now().isoformat())

folder = os.path.join(".github", "badges")

def generate_pylint_badge(ranking):
    ranking = float(ranking)
    color = "red"
    if ranking >= 8.0:
        color = "green"
    if ranking >= 6.0:
        color = "orange"


    badge_content = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="105" height="20" role="img" aria-label="Pylint: {ranking}%">
    <title>Pylint: {ranking}%</title>
    <linearGradient id="s" x2="0" y2="100%">
        <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
        <stop offset="1" stop-opacity=".1"/>
    </linearGradient>
    <clipPath id="r">
        <rect width="105" height="20" rx="3" fill="#fff"/>
    </clipPath>
    <g clip-path="url(#r)">
        <rect width="70" height="20" fill="#555"/>
        <rect x="70" width="35" height="20" fill="{color}"/>
        <rect width="105" height="20" fill="url(#s)"/>
    </g>
    <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="11px">
        <text aria-hidden="true" x="35" y="15" fill="#010101" fill-opacity=".3">Pylint</text>
        <text x="35" y="14">Pylint</text>
        <text aria-hidden="true" x="87.5" y="15" fill="#010101" fill-opacity=".3">{ranking}</text>
        <text x="87.5" y="14">{ranking}</text>
    </g>
    '{comment}'
</svg>
"""
    with open(os.path.join(folder, 'pylint-badge.svg'), 'w') as f:
        f.write(badge_content)


def get_pylint_rank(f):
    r = f.read()
    msg = "Your code has been rated at "
    i = r.find(msg) 
    i = i + len(msg)   
    rank = float(r[i:i+3])
    print(f" * [BADGE] Registered rank: {rank}")
    return rank


if __name__ == '__main__':
    try:
        with open('pylint_report.txt', 'r') as f:
            ranking = get_pylint_rank(f)
            generate_pylint_badge(ranking)
    except FileNotFoundError:
        print("Warning: pylint_report.txt not found. Skipping badge.")