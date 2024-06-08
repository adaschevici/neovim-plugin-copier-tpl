With my current setup Lazy is the plugin manager and plugins are loaded from the `lua/plugins` directory. Each file in there returns an object with the following format:

```lua
return {
	dir = "<path to local plugin directory>",
	name = "{{project_name}}",
	config = function()
		require("{{project_name}}").setup()
	end,
}
```

