![larkin-mcp](https://github.com/user-attachments/assets/ff8ff390-e9c9-4ddd-bc8a-e8dbecbab248)

# yourname-mcp

this is a template for creating personalized MCP servers. You can see [larkin-mcp](https://github.com/johnlarkin1/larkin-mcp) as an example, or check out my blog post about it [here](https://johnlarkin1.github.io/2025/larkin-mcp). It's technically a slightly more slimmed down version given I only really am trying to support `uvx` + `pypi` installs...

# demo

![demo](https://github.com/user-attachments/assets/724f5074-8230-49bb-8082-6e7d659b2952)
(sorry in advance about the low rez)

## tech

this is using [`copier`](https://copier.readthedocs.io/) which is basically a more up to date `cookiecutter` + `jinja` project. I honestly hadn't heard of it before asking ChatGPT if there were alternatives or more up to date projects. But here we are.

## what this creates

a MCP server that exposes your professional information (or really whatever you want to throw in there) to LLMs that have MCP connection (codex, claude code, claude desktop).

## getting started

this should really be all you need to do:

### without cloning:

```bash
$ YOURNAME='TODO' # PUT YOUR ACTUAL NAME HERE
$ brew install copier # (macos or linux... sorry windows)
$ copier copy gh:johnlarkin1/yourname-mcp $YOURNAME-mcp
```

### with cloning:

```bash
$ brew install copier # or again uv tool install copier
$ YOURNAME='TODO' # PUT YOUR ACTUAL NAME HERE
$ git clone https://github.com/johnlarkin1/yourname-mcp.git
$ copier copy yourname-mcp my-mcp-project
```

### answer questions!

Summary of what you're going to be asked for:

| Variable            | Description              | Example                            |
| ------------------- | ------------------------ | ---------------------------------- |
| `project_name`      | PyPI package name        | `johnsmith-mcp`                    |
| `person_full_name`  | Your full name           | `John Smith`                       |
| `person_first_name` | First name (for prompts) | `John`                             |
| `uri_scheme`        | Resource URI scheme      | `smith` (creates `smith://resume`) |
| `github_username`   | Your GitHub username     | `johnsmith`                        |
| `email`             | Your email               | `john@example.com`                 |
| `website_url`       | Your website (optional)  | `https://johnsmith.dev`            |
| `location`          | Your location (optional) | `New York, NY`                     |

### populate markdown files

populate this stuff!

```
src/resources/content/
├── bio.md           # Your biography
├── contact.md       # Contact information (pre-filled from prompts)
├── projects.md      # Your projects
├── skills.md        # Technical skills
├── work.md          # Work experience
└── resume/
    └── resume.md    # Full resume
```

### testing

```bash
cd my-mcp-project/$YOURNAME-mcp
uv sync
uv run pytest
uv run $YOURNAME-mcp
```

### publishing

note, this is a bit more involved. Feel free to email me about it, or ask ChatGPT / Claude, but you'll want to set up a PyPi account if you want to actually publish it.

```bash
uv build
uv publish  # Requires PyPI token
```

## using your local version (no pypi needed)

if you don't want to deal with pypi, you can just point claude desktop to your local project. the key is using `uv run --directory` to tell uv where your project lives:

```json
{
  "mcpServers": {
    "yourname-mcp": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/absolute/path/to/your/yourname-mcp",
        "yourname-mcp"
      ]
    }
  }
}
```

so if your project is at `~/code/johnsmith-mcp`, it'd look like:

```json
{
  "mcpServers": {
    "johnsmith-mcp": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/Users/johnsmith/code/johnsmith-mcp",
        "johnsmith-mcp"
      ]
    }
  }
}
```

just make sure you've run `uv sync` in your project directory first!

## using your published version

after you've published it, you can set this up in claude code or you can basically extend your claude_desktop.config. the config is cleaner since `uvx` fetches it automatically.

here's an example for mine:

```bash
╭─johnlarkin@Mac ~/Documents/coding/yourname-mcp-proj
╰─➤  vim ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

you'll want a similar path. And then you'll have something like:

```json
{
  "mcpServers": {
    "yourname-mcp": {
      "command": "uvx",
      "args": ["yourname-mcp"]
    }
  }
}
```

or for local (from within your project directory):

```json
{
  "mcpServers": {
    "yourname-mcp": {
      "command": "uv",
      "args": ["run", "yourname-mcp"]
    }
  }
}
```

## what's included:

> [!NOTE]  
> This section is Ai generated:

### Resources

Your MCP server exposes these resources (via custom URI scheme):

- `{scheme}://resume` - Full resume markdown
- `{scheme}://bio` - Biography
- `{scheme}://projects` - Project portfolio
- `{scheme}://contact` - Contact information
- `{scheme}://skills` - Technical skills
- `{scheme}://work` - Work history

### Tools

- `get_resume()`, `get_bio()`, `get_projects()`, etc. - Retrieve specific content
- `search_info(query)` - Search across all resources
- `health_check()` - Check server status

### Prompts

Pre-built prompts for common use cases:

- `summarize_for_role(role)` - Tailored summary for a job role
- `compare_to_job(job_description)` - Analyze fit for a job
- `interview_prep(role, company)` - Interview preparation
- `project_deep_dive(project_name)` - Detailed project info
