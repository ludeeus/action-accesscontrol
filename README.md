# ACCESSCONTROL

[![BuyMeCoffee][buymecoffeebedge]][buymecoffee]

_Check if the invoker has access._

## Example

```
workflow "Access control" {
  on = "push"
  resolves = ["Access control"]
}


action "Access control" {
  uses = "ludeeus/action-accesscontroll@master"
  env = {
    ACTION_LEVEL = "admin"
  }
  secrets = ["GITHUB_TOKEN"]
}
```

## ENV VARS

ENV | description
-- | --
`ACTION_LEVEL` | The level of access the user will need to pass this check, can be `admin`, `write` or `read`.

[buymecoffee]: https://www.buymeacoffee.com/ludeeus
[buymecoffeebedge]: https://camo.githubusercontent.com/cd005dca0ef55d7725912ec03a936d3a7c8de5b5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6275792532306d6525323061253230636f666665652d646f6e6174652d79656c6c6f772e737667
