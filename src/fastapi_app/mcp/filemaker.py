from .hub import hub_mcp
from ..services.filemaker import list_layouts, find_records

@hub_mcp.tool()
def read_layout() -> dict:
    """Read all layout's name from FileMaker database.

    """
    layouts = list_layouts()
    return layouts

@hub_mcp.tool()
def read_record(layout: str, query: list[dict]) -> list[dict]:
    """Find records from FileMaker database.

    Available layouts and fields( layout:fields ):
    - 問合せ_mcp_detail: d_問合せ日, t_経路, t_新規_display, t_課金_display, t_勤務形態, v_氏名
    - 成約_mcp_list: d_成約日, d_入金予定日, t_勤務形態, v_氏名, n_金額_税別
    - 成約_mcp_detail: d_成約日, d_入金予定日, t_勤務形態, v_氏名, n_金額_税別
    - 入金_mcp_detail: d_成約日, d_入金予定日, n_手数料料率, n_金額_税別
    - 成績_mcp_detail: v_成約日, c_成績計上期, v_経路, n_金額_税別_請求書未発行含め

    Query example:
        [{"d_問合せ日": "06/01/2026...06/30/2026"}]
        [{"d_問合せ日": "08/25/2026..."}]
        [{"d_問合せ日": "...08/25/2026"}]
        [{"t_経路": "M3", "t_課金_display": "課金"}]
    """

    records = find_records(layout=layout, query=query)
    return records["response"]["data"]
