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
        self.set_auto_page_break(auto=True, margin=12)
        # Use system Arial for Unicode support (en-dashes, bullets, etc.)
        self.add_font("DejaVu", "", fname="/System/Library/Fonts/Supplemental/Arial.ttf")
        self.add_font("DejaVu", "B", fname="/System/Library/Fonts/Supplemental/Arial Bold.ttf")
        self.add_font("DejaVu", "I", fname="/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf")
        self.add_page()
        self.set_margins(left=15, top=13, right=15)
        self.set_x(15)
        self.set_y(13)
        self.content_width = self.w - 30  # 15mm margins each side
        self.tab = 8  # 1-tab indent for section content
        self.indented_width = self.content_width - self.tab

    def header_section(self):
        # Name
        self.set_font("DejaVu", "B", 20)
        self.set_text_color(*BLACK)
        self.cell(self.content_width, 9, "Atul Agarwal", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

        # Subtitle
        self.set_font("DejaVu", "", 11)
        self.set_text_color(*ACCENT)
        self.cell(self.content_width, 5, "Protocol Engineer & DeFi Founder", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

        # Contact
        self.set_font("DejaVu", "", 8)
        self.set_text_color(*GRAY)
        self.cell(self.content_width, 4,
                  "atulagarwal893@gmail.com  ·  x.com/0xshinobii  ·  github.com/0xshinobii  ·  atulagarwal.dev  ·  Goa, India (Remote)",
                  align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def section_line(self):
        self.set_draw_color(*LINE_COLOR)
        y = self.get_y()
        self.line(15, y, self.w - 15, y)
        self.ln(3)

    def section_title(self, title):
        self.section_line()
        self.set_font("DejaVu", "B", 11)
        self.set_text_color(*BLACK)
        self.cell(self.content_width, 5, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def body_text(self, text):
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*DARK)
        self.set_x(self.l_margin + self.tab)
        self.multi_cell(self.indented_width, 4.2, text, new_x="LMARGIN", new_y="NEXT")

    def job_header(self, title, date):
        self.ln(2)
        self.set_font("DejaVu", "B", 9.5)
        self.set_text_color(*BLACK)
        date_w = self.get_string_width(date) + 4
        title_w = self.indented_width - date_w
        self.set_x(self.l_margin + self.tab)
        self.cell(title_w, 4.5, title, new_x="RIGHT", new_y="TOP")
        self.set_font("DejaVu", "I", 9)
        self.set_text_color(*GRAY)
        self.cell(date_w, 4.5, date, align="R", new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def job_desc(self, text):
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*GRAY)
        self.set_x(self.l_margin + self.tab)
        self.multi_cell(self.indented_width, 4.2, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.5)

    def sub_heading(self, text):
        self.ln(1.5)
        self.set_font("DejaVu", "B", 9)
        self.set_text_color(*DARK)
        self.set_x(self.l_margin + self.tab)
        self.cell(self.indented_width, 4.2, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.5)

    def bullet(self, text):
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*DARK)
        bullet_indent = 3
        bullet_w = 5
        x = self.l_margin + self.tab + bullet_indent
        self.set_x(x)
        self.cell(bullet_w, 4.2, "•", new_x="RIGHT", new_y="TOP")
        self.multi_cell(self.indented_width - bullet_indent - bullet_w, 4.2, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.3)

    def skill_line(self, label, text):
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*DARK)
        self.set_x(self.l_margin + self.tab)
        label_w = self.get_string_width(label + ": ")
        self.set_font("DejaVu", "B", 9)
        self.cell(label_w, 4.2, label + ":", new_x="RIGHT", new_y="TOP")
        self.set_font("DejaVu", "", 9)
        self.cell(1, 4.2, " ", new_x="RIGHT", new_y="TOP")
        remaining_w = self.indented_width - label_w - 1
        # Check if text fits in one line
        if self.get_string_width(text) <= remaining_w:
            self.cell(remaining_w, 4.2, text, new_x="LMARGIN", new_y="NEXT")
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
                        self.cell(remaining_w, 4.2, line, new_x="LMARGIN", new_y="NEXT")
                        first_line = False
                    else:
                        self.set_x(self.l_margin + self.tab)
                        self.cell(self.indented_width, 4.2, line, new_x="LMARGIN", new_y="NEXT")
                    line = word
            if line:
                if first_line:
                    self.cell(remaining_w, 4.2, line, new_x="LMARGIN", new_y="NEXT")
                else:
                    self.set_x(self.l_margin + self.tab)
                    self.cell(self.indented_width, 4.2, line, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.5)

    def edu_line(self, school, degree):
        self.set_font("DejaVu", "B", 9)
        self.set_text_color(*DARK)
        self.set_x(self.l_margin + self.tab)
        school_w = self.get_string_width(school)
        self.cell(school_w, 4.5, school, new_x="RIGHT", new_y="TOP")
        self.set_font("DejaVu", "", 9)
        self.cell(self.indented_width - school_w, 4.5, " — " + degree, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def writing_bullet(self, title, url, description):
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*DARK)
        bullet_indent = 3
        bullet_w = 5
        x = self.l_margin + self.tab + bullet_indent
        self.set_x(x)
        self.cell(bullet_w, 4.2, "•", new_x="RIGHT", new_y="TOP")
        # Title in accent color
        self.set_text_color(*ACCENT)
        title_w = self.get_string_width(title)
        self.cell(title_w, 4.2, title, link=url, new_x="RIGHT", new_y="TOP")
        # Description in dark
        self.set_text_color(*DARK)
        remaining = " — " + description
        self.multi_cell(self.indented_width - bullet_indent - bullet_w - title_w, 4.2, remaining, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.3)


def build_pdf(filename):
    pdf = ResumePDF()

    # Header
    pdf.header_section()

    # Summary
    pdf.section_title("Summary")
    pdf.body_text(
        "Protocol engineer and DeFi founder with 5+ years shipping production-grade blockchain "
        "infrastructure. Co-founded two DeFi protocols from zero to production: a perpetual futures "
        "exchange with a decentralized limit order book (DLOB) on a custom Avalanche Subnet, and a "
        "leveraged lending protocol on Aptos that peaked at $7M TVL. Own smart contracts end-to-end "
        "across Solidity and Move; deep expertise in AMM invariant mathematics, order book systems, "
        "liquidation engines, and cross-chain bridging."
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
    pdf.bullet("Solidity smart contracts and protocol integrations for a stablecoin index protocol aggregating yield-bearing stablecoins")

    # MediaTek
    pdf.job_header("MediaTek — Chip Design Engineer", "2018 – 2021")
    pdf.bullet("3 years designing digital circuits for production SoCs — timing closure, RTL verification, physical design")
    pdf.bullet("Built the engineering rigor (edge-case thinking, constraint optimization) that carries into smart contract work")

    # Technical Skills
    pdf.section_title("Technical Skills")
    pdf.skill_line("Languages", "Solidity (Foundry, Hardhat), Move (Aptos), Rust, TypeScript, Python")
    pdf.skill_line("Protocol Design",
                   "Perpetual futures exchange (vAMM, funding rates, margin systems), lending & borrowing platforms "
                   "(leveraged lending, liquidation engines), DLOB architecture, AMM invariants (StableSwap, CurveCrypto), "
                   "cross-chain bridging (LayerZero)")
    pdf.skill_line("Chains", "Ethereum/EVM, Avalanche Subnets, Aptos/MoveVM")
    pdf.skill_line("Backend", "Node.js, PostgreSQL, Docker, bots & indexers")

    # Education
    pdf.section_title("Education")
    pdf.edu_line("Indian Institute of Technology (IIT) Delhi", "Master of Technology (M.Tech)")
    pdf.edu_line("Indian Institute of Technology (IIT) Jodhpur", "Bachelor of Technology (B.Tech)")

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
