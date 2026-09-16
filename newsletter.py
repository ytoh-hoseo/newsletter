#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from jinja2 import Template
import markdown2
from pathlib import Path
from datetime import datetime
from premailer import transform


def generate_newsletter(content_file, template_file, output_file):
    """
    Markdown 뉴스레터를 HTML로 변환

    Args:
        content_file: Markdown 파일 경로
        template_file: HTML 템플릿 파일 경로
        output_file: 출력 HTML 파일 경로
    """

    # Markdown 파일 읽기
    with open(content_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Markdown을 HTML로 변환
    html_content = markdown2.markdown(
        md_content, extras=["tables", "fenced-code-blocks", "strike"]
    )

    # HTML 템플릿 읽기
    with open(template_file, "r", encoding="utf-8") as f:
        template_str = f.read()

    # Jinja2 템플릿 렌더링
    template = Template(template_str)
    final_html = template.render(
        title="호서대학교 게임소프트웨어학과 뉴스레터",
        content=html_content,
        date=datetime.now().strftime("%Y년 %m월 %d일"),
    )

    # 메일에 복사해도 서식이 유지되도록 CSS를 각 요소에 직접 적용
    final_html = transform(
        final_html, allow_network=False, include_star_selectors=True
    )

    # 결과 저장
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"✅ 뉴스레터 생성 완료: {output_file}")
    return output_file


if __name__ == "__main__":
    generate_newsletter(
        content_file="content.md",
        template_file="template.html",
        output_file="output/newsletter.html",
    )
