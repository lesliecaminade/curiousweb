#adjustments
DOCUMENT_TYPE = 'article'
COLUMNS = 2


LATEX_PREAMBLE = f"""\\documentclass{{{DOCUMENT_TYPE}}} %book, report, article, letter, slides

    % General document formatting
    \\usepackage[margin=0.7in]{{geometry}}
    \\usepackage[parfill]{{parskip}}
    \\usepackage[utf8]{{inputenc}}
    \\usepackage{{multicol}}

    % Related to math
    \\usepackage{{amsmath,amssymb,amsfonts,amsthm}}

    %other
    \\usepackage{{graphicx}}

\\begin{{document}}
\\begin{{multicols*}}{{{COLUMNS}}}
"""

LATEX_TRAILER = f"""\\end{{multicols*}}
\\end{{document}}"""


LATEX_ITEM_PREFIX = f"""\\paragraph {{Question}} """


LATEX_SOLUTION_PREFIX = f"""\\begin{{align*}}"""

LATEX_SOLUTION_SPLIT = f"""\\end{{align*}}
\\begin{{align*}}"""

LATEX_SOLUTION_SUFFIX = f"""\\end{{align*}}
"""

LATEX_END = f"""\\\\"""

LP = f"""\\left("""
RP = f"""\\right)"""

lp = LP
rp = RP

def sub(main, sub):
	return f"""{{{main}}}_{{{sub}}}"""

def paren(main):
	return f"""{lp}{main}{rp}"""

def integral(function, a, b, integration_variable):
	return f"""\\int_{a}^{b} \\! {function} \\, \\mathrm{{d}}{integration_variable}."""

def text(main):
	return f"""\\text{{ {text}}}"""

def fraction(num, denom):
	return f"""\\frac{{{num}}} {{denom}}"""

def newline():
	return f"""& \\\\"""

def sqrt(function):
	return f"""\\sqrt{{{function}}}"""
