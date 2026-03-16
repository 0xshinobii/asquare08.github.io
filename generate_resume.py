#!/usr/bin/env python3
"""Generate Atul Agarwal's resume PDF from website content using fpdf2."""

from fpdf import FPDF

ACCENT = (43, 123, 185)
BLACK = (26, 26, 26)
DARK = (51, 51, 51)
GRAY = (85, 85, 85)
LINE_COLOR = (204, 204, 204)

class ResumePDF(FPDF):
    def __init__(self):
        super().__init__(format="letter")
        self.set_auto_page_break(auto=False)
        # Use system Arial for Unicode support (en-dashes, bullets, etc.)
        self.add_font("DejaVu", "", fname="/System/Library/Fonts/Supplemental/Arial.ttf")
        self.add_font("DejaVu", "B", fname="/System/Library/Fonts/Supplemental/Arial Bold.ttf")
        self.add_font("DejaVu", "I", fname="/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf")
        self.add_page()
        self.set_margins(left=15, top=12, right=15)
        self.set_x(15)
        self.set_y(12)
        self.content_width = self.w - 30  # 15mm margins each side
        self.tab = 8  # 1-tab indent for section content
        self.indented_width = self.content_width - self.tab

    def header_section(self):
        # Name
        self.set_font("DejaVu", "B", 20)
        self.set_text_color(*BLACK)
        self.cell(self.content_width, 8, "Atul Agarwal", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(1.5)

        # Subtitle
        self.set_font("DejaVu", "", 11)
        self.set_text_color(*ACCENT)
        self.cell(self.content_width, 5, "Protocol Engineer & Builder", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(1.5)

        # Contact
        self.set_font("DejaVu", "", 8)
        self.set_text_color(*GRAY)
        self.cell(self.content_width, 4,
                  "atulagarwal893@gmail.com  ·  x.com/0xshinobii  ·  atulagarwal.dev  ·  Goa, India (Remote)",
                  align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def section_line(self):
        self.set_draw_color(*LINE_COLOR)
        y = self.get_y()
        self.line(15, y, self.w - 15, y)
        self.ln(2)

    def section_title(self, title):
        self.section_line()
        self.set_font("DejaVu", "B", 11)
        self.set_text_color(*BLACK)
        self.cell(self.content_width, 5, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1.5)

    def body_text(self, text):
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*DARK)
        self.set_x(self.l_margin + self.tab)
        self.multi_cell(self.indented_width, 4, text, new_x="LMARGIN", new_y="NEXT")

    def job_header(self, title, date):
        self.ln(1.5)
        self.set_font("DejaVu", "B", 9.5)
        self.set_text_color(*BLACK)
        date_w = self.get_string_width(date) + 4
        title_w = self.indented_width - date_w
        self.set_x(self.l_margin + self.tab)
        self.cell(title_w, 4.5, title, new_x="RIGHT", new_y="TOP")
        self.set_font("DejaVu", "I", 9)
        self.set_text_color(*GRAY)
        self.cell(date_w, 4.5, date, align="R", new_x="LMARGIN", new_y="NEXT")
        self.ln(0.5)

    def job_desc(self, text):
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*GRAY)
        self.set_x(self.l_margin + self.tab)
        self.multi_cell(self.indented_width, 4, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.3)

    def sub_heading(self, text):
        self.ln(1)
        self.set_font("DejaVu", "B", 9)
        self.set_text_color(*DARK)
        self.set_x(self.l_margin + self.tab)
        self.cell(self.indented_width, 4, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.3)

    def bullet(self, text):
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*DARK)
        bullet_indent = 3
        bullet_w = 5
        x = self.l_margin + self.tab + bullet_indent
        self.set_x(x)
        self.cell(bullet_w, 4, "•", new_x="RIGHT", new_y="TOP")
        self.multi_cell(self.indented_width - bullet_indent - bullet_w, 4, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.2)

    def skill_line(self, label, text):
        self.ln(1)
        self.set_font("DejaVu", "B", 9)
        self.set_text_color(*DARK)
        self.set_x(self.l_margin + self.tab)
        label_w = self.get_string_width(label + ": ")
        self.cell(label_w, 4, label + ": ", new_x="RIGHT", new_y="TOP")
        self.set_font("DejaVu", "", 9)
        remaining_w = self.indented_width - label_w
        # Check if text fits in one line
        if self.get_string_width(text) <= remaining_w:
            self.cell(remaining_w, 4, text, new_x="LMARGIN", new_y="NEXT")
        else:
            # First line remainder, continuation lines also at tab indent
            words = text.split(" ")
            line = ""
            first_line = True
            for word in words:
                test = line + (" " if line else "") + word
                w = remaining_w if first_line else self.indented_width
                if self.get_string_width(test) <= w:
                    line = test
                else:
                    if first_line:
                        self.cell(remaining_w, 4, line, new_x="LMARGIN", new_y="NEXT")
                        first_line = False
                    else:
                        self.set_x(self.l_margin + self.tab)
                        self.cell(self.indented_width, 4, line, new_x="LMARGIN", new_y="NEXT")
                    line = word
            if line:
                if first_line:
                    self.cell(remaining_w, 4, line, new_x="LMARGIN", new_y="NEXT")
                else:
                    self.set_x(self.l_margin + self.tab)
                    self.cell(self.indented_width, 4, line, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.3)

    def edu_line(self, school, degree, year):
        self.set_font("DejaVu", "I", 9)
        self.set_text_color(*GRAY)
        year_w = self.get_string_width(year) + 4
        self.set_font("DejaVu", "B", 9)
        self.set_text_color(*DARK)
        self.set_x(self.l_margin + self.tab)
        school_w = self.get_string_width(school)
        self.cell(school_w, 4.5, school, new_x="RIGHT", new_y="TOP")
        self.set_font("DejaVu", "", 9)
        deg_text = " — " + degree
        deg_w = self.indented_width - school_w - year_w
        self.cell(deg_w, 4.5, deg_text, new_x="RIGHT", new_y="TOP")
        self.set_font("DejaVu", "I", 9)
        self.set_text_color(*GRAY)
        self.cell(year_w, 4.5, year, align="R", new_x="LMARGIN", new_y="NEXT")
        self.ln(0.5)

    def writing_bullet(self, title, url, description):
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*DARK)
        bullet_indent = 3
        bullet_w = 5
        x = self.l_margin + self.tab + bullet_indent
        self.set_x(x)
        self.cell(bullet_w, 4, "•", new_x="RIGHT", new_y="TOP")
        # Title in accent color
        self.set_text_color(*ACCENT)
        title_w = self.get_string_width(title)
        self.cell(title_w, 4, title, link=url, new_x="RIGHT", new_y="TOP")
        # Description in dark
        self.set_text_color(*DARK)
        remaining = " — " + description
        self.multi_cell(self.indented_width - bullet_indent - bullet_w - title_w, 4, remaining, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.2)


def build_pdf(filename):
    pdf = ResumePDF()

    # Header
    pdf.header_section()

    # Summary
    pdf.section_title("Summary")
    pdf.body_text(
        "Started in chip design at MediaTek, taught myself software engineering, and jumped to DeFi in 2021. "
        "Co-founded two protocols from zero to production — a perpetual futures exchange on Avalanche and a "
        "leveraged lending protocol on Aptos that peaked at $7M TVL. The common thread: going deep on hard "
        "problems — porting Newton's method solvers to Solidity, designing a custom Avalanche Subnet where "
        "validators act as order matchers, or picking up Move to build on an early ecosystem. Currently "
        "exploring the intersection of AI and finance — the agent economy, autonomous economic actors, "
        "and machine-to-machine payment rails."
    )

    # Experience
    pdf.section_title("Experience")

    # Moar Market
    pdf.job_header("Moar Market — Founder", "2024 – Present")
    pdf.job_desc("Leveraged lending protocol on Aptos with integrations across Hyperion, Tapp, and Panora.")
    pdf.bullet("Live protocol with $2M TVL, peaked at $7M in January 2026")
    pdf.bullet("Owned all Move smart contracts: collateral vaults, interest rate models, oracle integrations, liquidation logic")
    pdf.bullet("Co-built backend: indexer, liquidator bot, risk monitoring, and API layer")
    pdf.bullet("Defined risk parameters, collateral factors, and liquidation incentives for multi-asset markets")

    # Hubble Exchange
    pdf.job_header("Hubble Exchange — Co-Founder & Protocol Engineer", "2021 – 2024")
    pdf.job_desc("Decentralized perpetual futures exchange on Avalanche — evolved from vAMM (V1) to DLOB on custom Subnet (V2).")
    pdf.sub_heading("V2: Decentralized Limit Order Book (DLOB) on Avalanche Subnet")
    pdf.bullet("Owned all Solidity smart contracts for order-book DEX on custom Avalanche Subnet with validators as order matchers")
    pdf.bullet("Built cross-chain asset bridge using LayerZero (lock-mint mechanism) for L1-to-subnet transfers")
    pdf.bullet("Co-built liquidator bot, order-matching service, and monitoring infrastructure")
    pdf.sub_heading("V1: Virtual AMM Perpetuals")
    pdf.bullet("Implemented CurveCrypto invariant in Solidity — Newton's method solver for on-chain price computation")
    pdf.bullet("Designed margin engine, funding rate mechanism, and multi-collateral vault system")

    # DefiDollar
    pdf.job_header("DefiDollar — Smart Contract Engineer", "2021")
    pdf.job_desc("Smart contract development for a stablecoin index protocol on Ethereum — aggregated yield-bearing stablecoins into a single diversified token.")

    # Deploy
    pdf.job_header("Deploy — Side Project", "2026")
    pdf.job_desc("MVP for an automated grid trading bot on Hyperliquid perpetual futures.")
    pdf.bullet("Event-driven TypeScript engine with RabbitMQ, PostgreSQL, and WebSocket-based order lifecycle management")

    # MediaTek
    pdf.job_header("MediaTek — Chip Design Engineer", "2017 – 2020")
    pdf.job_desc("Designed digital circuits for production SoCs — timing closure, RTL verification, and physical design across multiple chip tapeouts.")

    # Skills
    pdf.section_title("Skills")
    pdf.skill_line("Languages",
                   "Solidity (Foundry, Hardhat, EVM internals), Move (Aptos framework, resource model), "
                   "Rust, TypeScript, Python")
    pdf.skill_line("Protocol Design",
                   "Perpetual futures (vAMM, funding rates, margin systems, liquidation engines), "
                   "lending & borrowing (leveraged lending, interest rate models, collateral management), "
                   "DLOB on custom L1/Subnet, AMM invariants (StableSwap, CurveCrypto, Newton's method solvers), "
                   "cross-chain bridging (LayerZero)")
    pdf.skill_line("Chains & Infra", "Ethereum/EVM, Avalanche (custom Subnets, validator operations), Aptos/MoveVM")
    pdf.skill_line("Backend & Tooling",
                   "PostgreSQL, RabbitMQ, Docker, monitoring; "
                   "event-driven architecture (WebSocket listeners, message queues, state machines)")

    # Education
    pdf.section_title("Education")
    pdf.edu_line("Indian Institute of Technology (IIT) Delhi", "Master of Technology (M.Tech)", "2017")
    pdf.edu_line("Indian Institute of Technology (IIT) Jodhpur", "Bachelor of Technology (B.Tech)", "2015")

    # Writing
    pdf.section_title("Writing")
    pdf.writing_bullet(
        "Understanding the Curve AMM: StableSwap Invariant",
        "https://atulagarwal.dev/posts/curveamm/stableswap/",
        "Newton's method, swap mechanics, bonding curve math"
    )
    pdf.writing_bullet(
        "Hubble vAMM: CurveCrypto Invariant",
        "https://atulagarwal.dev/posts/hubblevamm/",
        "extending Curve's invariant to volatile-asset perpetual futures"
    )

    pdf.output(filename)
    print(f"Generated {filename}")


if __name__ == "__main__":
    build_pdf("/Users/atulagarwal/mystuff/asquare8.github.io/atul_agarwal_resume.pdf")
