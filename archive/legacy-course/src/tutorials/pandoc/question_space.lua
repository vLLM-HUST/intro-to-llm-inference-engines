local in_question_section = false

local function header_text(el)
  return pandoc.utils.stringify(el.content)
end

local function answer_line_count(blocks)
  local text = pandoc.utils.stringify(blocks)

  if text:find("%[伪代码题%]") then
    return 4
  end
  if text:find("%[计算题%]") then
    return 3
  end
  if text:find("%[简答题%]") then
    return 2
  end
  if text:find("%[多选题%]") then
    return 1
  end
  if text:find("%[单选题%]") then
    return 1
  end
  if text:find("%[判断题%]") then
    return 1
  end

  return 2
end

local function answer_box_height(blocks)
  local text = pandoc.utils.stringify(blocks)

  if text:find("%[伪代码题%]") then
    return "5.0cm"
  end
  if text:find("%[简答题%]") then
    return "2.8cm"
  end

  return nil
end

local function answer_line_blocks(count)
  local blocks = {}

  for _ = 1, count do
    blocks[#blocks + 1] = pandoc.RawBlock("latex", "\\noindent\\rule{\\linewidth}{0.4pt}")
    blocks[#blocks + 1] = pandoc.RawBlock("latex", "\\vspace{0.7cm}")
  end

  return blocks
end

local function answer_box_blocks(height)
  local blocks = {}

  blocks[#blocks + 1] = pandoc.RawBlock(
    "latex",
    "\\begingroup\\setlength{\\fboxsep}{8pt}\\setlength{\\fboxrule}{0.5pt}"
  )
  blocks[#blocks + 1] = pandoc.RawBlock(
    "latex",
    "\\noindent\\fcolorbox{black!25}{black!4}{\\parbox[t][" .. height .. "][t]{\\dimexpr\\linewidth-2\\fboxsep-2\\fboxrule\\relax}{\\strut}}"
  )
  blocks[#blocks + 1] = pandoc.RawBlock("latex", "\\par\\endgroup")

  return blocks
end

function Header(el)
  if el.level == 2 then
    local text = header_text(el)
    if text == "题目" then
      in_question_section = true
    elseif text == "参考答案" then
      in_question_section = false
    end
  end

  return el
end

function OrderedList(el)
  if not in_question_section then
    return el
  end

  local updated_items = {}

  for _, item in ipairs(el.content) do
    local blocks = item
    local box_height = answer_box_height(blocks)
    local answer_blocks

    if box_height then
      answer_blocks = answer_box_blocks(box_height)
    else
      local line_count = answer_line_count(blocks)
      answer_blocks = answer_line_blocks(line_count)
    end

    for _, block in ipairs(answer_blocks) do
      blocks[#blocks + 1] = block
    end

    updated_items[#updated_items + 1] = blocks
  end

  return pandoc.OrderedList(updated_items, el.listAttributes)
end