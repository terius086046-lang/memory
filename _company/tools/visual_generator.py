# visual_generator.py
import json
import os
from server import process_request # 서버에서 요청 처리 함수를 가져옴

def generate_design_mockup(project_id: str, template_id: str):
    """
    주어진 프로젝트 ID와 템플릿 ID를 기반으로 AI 디자인 모형을 생성하도록 서버에 요청합니다.
    """
    try:
        # 1. 필요한 데이터 로드 (데이터베이스 연동 시뮬레이션)
        with open(f"_company/data/projects.json", 'r') as f:
            project_data = json.load(f)

        with open(f"_company/data/quote_templates.json", 'r') as f:
            template_data = json.load(f)

        # 2. AI 프롬프트 구성
        template_info = next((t for t in template_data['templates'] if t['template_id'] == template_id), None)
        project_info = next((p for p in project_data['projects'] if p['project_id'] == project_id), None)

        if not template_info or not project_info:
            return {"error": "Template or Project data not found."}

        # 3. AI에게 전달할 프롬프트 구성
        prompt = f"""
        당신은 최고 수준의 인테리어 아키텍트이자 네오-글래스모피즘 스타일 전문가입니다.
        다음 프로젝트 정보를 바탕으로, {template_info['name']} 템플릿을 적용하여 시각화된 대시보드 Mockup 이미지를 생성해야 합니다.

        [프로젝트 정보]
        ID: {project_id}
        고객명: {project_info['client_name']}
        프로젝트 유형: {project_info['project_type']}
        원하는 스타일: {template_info['layout_config']['style']}
        핵심 색상 팔레트: {template_info['layout_config']['color_palette']}
        포함할 항목(Line Items): {template_info['line_items']}

        위 정보를 바탕으로, 사용자가 업로드한 데이터를 반영하여 가장 권위 있고 구조적인 디자인 대시보드 이미지의 구성을 제안하고 생성하세요.
        """

        # 4. 서버 함수 호출 (실제 AI 호출)
        result = process_request(prompt)
        return result

    except Exception as e:
        return {"error": f"Design generation failed: {e}"}

if __name__ == "__main__":
    # 테스트 실행 예시 (실제 서버 환경에서 호출될 예정)
    print("--- Visual Generator Initialized ---")
    print("This script is designed to interface with the server to generate design mockups.")
    # 실제 실행은 서버가 구동된 후 API를 통해 이루어집니다.