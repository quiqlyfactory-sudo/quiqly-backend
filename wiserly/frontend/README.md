# WISeRly Frontend: Carbon Mint Design System

## Part of Quiqly's **Integrated UI Layer**

The WISeRly frontend brings all 4 intelligences to life with the **Carbon Mint** design system: Neo-Mint (#A8E6CF) on True Charcoal (#0B0D10), with Bricolage Grotesque personality and Inter clarity.

See: [DESIGN_SYSTEM.md](../DESIGN_SYSTEM.md) | [QUIQLY_ARCHITECTURE.md](../../QUIQLY_ARCHITECTURE.md)

---

## What It Includes

**theme.css** - Design tokens and component library
- Colors: Charcoal, Neo-Mint, Grays, Off-White
- Typography: Bricolage Grotesque (headings), Inter (body), JetBrains Mono (code)
- Components: Buttons, Cards, Status indicators, Grids, Flexbox layouts
- Accessibility: WCAG AA contrast, keyboard navigation, focus states

**index.html** - Landing page + feature showcase
- Hero section with CTA
- 6 feature cards (AskVault, ComplianceShield, MarketingForge, MoneyCard, GodMode, SocialGhost)
- Pricing section ($2,499 lifetime)
- Responsive design
- Dark mode first (light mode fallback)

## Design Principles

🎨 **Progressive Interface** - Simple for beginners, detailed code view for pros  
🌙 **Dark Mode First** - Reduces eye strain  
🎯 **Action Cards** - Big, clear tiles over complex menus  
👁️ **Observability** - Always show what AI is doing in real-time  

## Color Reference

| Name | Hex | Usage |
|---|---|---|
| True Charcoal | #0B0D10 | Main background |
| Neo-Mint | #A8E6CF | Active states, CTAs, highlights |
| Secondary Gray | #1E2125 | Card backgrounds |
| Tertiary Gray | #2A2D32 | Borders, dividers |
| Off-White | #F5F5F5 | Body text |

## Typography

- **Headings**: Bricolage Grotesque (quirky, personality)
- **Body**: Inter (clean, 16px base)
- **Code**: JetBrains Mono (fixed-width)

## Components

### Buttons
```html
<button class="btn btn-primary">Primary Action</button>
<button class="btn btn-secondary">Secondary</button>
```

### Cards
```html
<div class="card">
  <div class="card-title">Feature Name</div>
  <div class="card-description">Description here</div>
  <span class="status-success">✅ Status</span>
</div>
```

### Status Indicators
- `.status-success` (Green) - ✅ Working
- `.status-warning` (Yellow) - ⚠️ Attention needed
- `.status-error` (Red) - ❌ Problem
- `.status-info` (Mint) - 🔵 Information

## Files

- `theme.css` - Global styles and component library
- `index.html` - Landing page
- `README.md` - This file

## Integration with 4 Intelligences

| Intelligence | Frontend Component |
|---|---|
| **Neuro-Symbolic** | AskVault card with verification badge |
| **Agentic** | GodMode status orbs, SocialGhost activity |
| **World Models** | MarketingForge video showcase, MoneyCard metrics |
| **Repository** | Feature showcase (same across all products) |

## Development

### Add a New Card
```html
<div class="card">
  <div class="card-title">🚀 Feature Name</div>
  <div class="card-description">What it does...</div>
  <span class="status-success">✅ Status</span>
</div>
```

### Customize Theme
Edit `:root` variables in `theme.css`:
```css
--color-mint: #A8E6CF;
--color-charcoal: #0B0D10;
```

## Next Steps

1. Build AskVault interactive demo
2. Add MoneyCard dashboard (real-time financials)
3. GodMode service status display
4. SocialGhost content feed
5. MarketingForge video player

---

*WISeRly Frontend. Built with Carbon Mint. Powered by Quiqly.*
