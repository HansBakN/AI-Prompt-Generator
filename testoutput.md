## Context Notes
```This pull request adds some basic functionality to a Blazor project in which users are able to track their bowling stats. 
It is one of the first pull requests that adds functionality to the UI, so it is very important that it follows the Blazor best practices, as it will set a precedent for the next features that will be implemented```

## Task Instructions
```Task:
  You are an AI-powered code reviewer. You will be provided with feature context and a set of Git diffs.

Objectives:
  1. Assess overall code quality, readability, and adherence to best practices of the language.
  2. Identify potential bugs, edge cases, and performance bottlenecks.
  3. Highlight security concerns and suggest fixes.
  4. Recommend improvements to naming, structure, and documentation.

Tone:
  Provide clear, concise, and actionable feedback. Prioritize critical issues first, followed by stylistic suggestions.

Output format: 
  List all changes you would make with an explanation. Then show the part of a file as it was originally and how you would change that part of the file to improve it. If new files need to be created output the whole file as you would create it.
```

## Project Structure (tracked files)
```
./
  .dockerignore
  .gitignore
  compose.yml
.github/
  workflows/sonarqube-analyze.yml
src/
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/BowlingTrackerSupreme.Blazor.Client.csproj
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/Pages/Counter.razor
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/Pages/Player.razor
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/Program.cs
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/_Imports.razor
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/wwwroot/appsettings.Development.json
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/wwwroot/appsettings.json
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.csproj
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/App.razor
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Layout/MainLayout.razor
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Layout/MainLayout.razor.css
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Layout/NavMenu.razor
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Layout/NavMenu.razor.css
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Error.razor
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Game.razor
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Games.razor
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Home.razor
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Player.razor
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Players.razor
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Weather.razor
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Routes.razor
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/_Imports.razor
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Controllers/GamesController.cs
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Controllers/PlayersController.cs
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Program.cs
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Properties/launchSettings.json
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/appsettings.development.json
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/wwwroot/app.css
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/wwwroot/bootstrap/bootstrap.min.css
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/wwwroot/bootstrap/bootstrap.min.css.map
  BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/wwwroot/images/favicon.png
  BowlingTrackerSupreme.Domain/BowlingTrackerSupreme.Domain.csproj
  BowlingTrackerSupreme.Domain/Models/FinalFrame.cs
  BowlingTrackerSupreme.Domain/Models/Frame.cs
  BowlingTrackerSupreme.Domain/Models/Game.cs
  BowlingTrackerSupreme.Domain/Models/Player.cs
  BowlingTrackerSupreme.Domain/Models/PlayerGame.cs
  BowlingTrackerSupreme.Domain/Models/Roll.cs
  BowlingTrackerSupreme.Domain/Services/BowlingScoreCalculator.cs
  BowlingTrackerSupreme.Infrastructure/BowlingTrackerSupreme.Infrastructure.csproj
  BowlingTrackerSupreme.Infrastructure/Database/BowlingTrackerSupremeDbContext.cs
  BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/FinalFrameConfiguration.cs
  BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/FrameConfiguration.cs
  BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/GameConfiguration.cs
  BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/PlayerConfiguration.cs
  BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/PlayerGameConfiguration.cs
  BowlingTrackerSupreme.Infrastructure/ServiceCollectionExtensions.cs
  BowlingTrackerSupreme.Migrations/BowlingTrackerSupreme.Migrations.csproj
  BowlingTrackerSupreme.Migrations/Migrations/20250125122446_Initial.Designer.cs
  BowlingTrackerSupreme.Migrations/Migrations/20250125122446_Initial.cs
  BowlingTrackerSupreme.Migrations/Migrations/20250125144934_AddedScoreToFrame.Designer.cs
  BowlingTrackerSupreme.Migrations/Migrations/20250125144934_AddedScoreToFrame.cs
  BowlingTrackerSupreme.Migrations/Migrations/20250125183500_AddedDateTimesToGames.Designer.cs
  BowlingTrackerSupreme.Migrations/Migrations/20250125183500_AddedDateTimesToGames.cs
  BowlingTrackerSupreme.Migrations/Migrations/20250225212756_AddedCreatedOnModifiedOn.Designer.cs
  BowlingTrackerSupreme.Migrations/Migrations/20250225212756_AddedCreatedOnModifiedOn.cs
  BowlingTrackerSupreme.Migrations/Migrations/BowlingTrackerSupremeDbContextModelSnapshot.cs
  BowlingTrackerSupreme.Migrations/SqlServerDbContextBuilderExtensions.cs
  BowlingTrackerSupreme.sln
```

## Change Summary
 31 files changed, 1001 insertions(+), 97 deletions(-)


## Commits
- **e9c4c1c** by Daniel Fly: Removed SonarQube build PR trigger
- **32be254** by Daniel Fly: Revert workflow-test
- **9fa92d6** by Daniel Fly: WIP: workflow-test
- **3bf2367** by Daniel Fly: Fixed SonarQube build after src folder
- **c297897** by Daniel Fly: WIP: Game and player view
- **00a2c79** by Daniel Fly: Added Games controller
- **fa957fb** by Daniel Fly: Added player list page
- **dc0e7bf** by Daniel Fly: Replaced header 'About' with bowling XiaoPang
- **47e1fd1** by Daniel Fly: Updated homepage
- **ad3614b** by Daniel Fly: Added player API controller and Create endpoint
- **3b51bdc** by Daniel Fly: Added CreatedOn and ModifiedOn to entities

## File Changes with Details
### Directory: .github
#### File: .github/workflows/sonarqube-analyze.yml
*Summary:* Removed SonarQube build PR trigger

**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/.github/workflows/sonarqube-analyze.yml b/.github/workflows/sonarqube-analyze.yml
index 0323835..0fce742 100644
--- a/.github/workflows/sonarqube-analyze.yml
+++ b/.github/workflows/sonarqube-analyze.yml
@@ -4,10 +4,6 @@ on:
   push:
     branches:
       - main
-  pull_request_target:
-    branches: 
-      - main
-
 
 jobs:
   build:
@@ -46,5 +42,5 @@ jobs:
         shell: powershell
         run: |
           .\.sonar\scanner\dotnet-sonarscanner begin /k:"BowlingTrackerSupreme" /d:sonar.token="${{ secrets.SONAR_TOKEN }}" /d:sonar.host.url="${{ secrets.SONAR_HOST_URL }}"
-          dotnet build
+          dotnet build .\src\
           .\.sonar\scanner\dotnet-sonarscanner end /d:sonar.token="${{ secrets.SONAR_TOKEN }}"

```

### Directory: src
#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/BowlingTrackerSupreme.Blazor.Client.csproj
*Summary:* Added player list page

**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/BowlingTrackerSupreme.Blazor.Client.csproj b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/BowlingTrackerSupreme.Blazor.Client.csproj
index 83962bc..7b7428a 100644
--- a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/BowlingTrackerSupreme.Blazor.Client.csproj
+++ b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/BowlingTrackerSupreme.Blazor.Client.csproj
@@ -1,4 +1,4 @@
-<Project Sdk="Microsoft.NET.Sdk.BlazorWebAssembly">
+﻿<Project Sdk="Microsoft.NET.Sdk.BlazorWebAssembly">
 
     <PropertyGroup>
         <TargetFramework>net8.0</TargetFramework>
@@ -9,8 +9,12 @@
     </PropertyGroup>
 
     <ItemGroup>
-        <PackageReference Include="Microsoft.AspNetCore.Components.WebAssembly" Version="8.0.11"/>
+        <PackageReference Include="Microsoft.AspNetCore.Components.WebAssembly" Version="8.0.11" />
         <PackageReference Include="Microsoft.EntityFrameworkCore.Relational" Version="8.0.12" />
     </ItemGroup>
 
+    <ItemGroup>
+      <ProjectReference Include="..\..\BowlingTrackerSupreme.Domain\BowlingTrackerSupreme.Domain.csproj" />
+    </ItemGroup>
+
 </Project>

```

#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/Pages/Counter.razor
*Summary:* Added player API controller and Create endpoint

**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/Pages/Counter.razor b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/Pages/Counter.razor
index 4e25819..a067da6 100644
--- a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/Pages/Counter.razor
+++ b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/Pages/Counter.razor
@@ -16,5 +16,4 @@
     {
         _currentCount++;
     }
-
 }
\ No newline at end of file

```

#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/Pages/Player.razor
*Summary:* Added player list page

**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/Pages/Player.razor b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/Pages/Player.razor
new file mode 100644
index 0000000..d77fc25
--- /dev/null
+++ b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/Pages/Player.razor
@@ -0,0 +1,42 @@
+﻿@page "/player"
+@using BowlingTrackerSupreme.Domain.Models;
+@inject HttpClient httpClient
+@inject NavigationManager NavigationManager
+
+<h3>Add new player</h3>
+
+<EditForm Model="@player" OnValidSubmit="SavePlayer">
+	<DataAnnotationsValidator />
+	<div class="mb-3">
+		<label class="form-label">Name</label>
+		<div class="col-mb-4">
+			<InputText class="form-control" @bind-Value="player.Name" />
+		</div>
+		<ValidationMessage For="@(() => player.Name)" />
+	</div>
+
+	<div class="form-group">
+		<button type="submit" class="btn btn-primary">Add</button>
+		<button class="btn btn-cancel" @onclick="Cancel">Cancel</button>
+	</div>
+</EditForm>
+
+
+@code {
+
+	protected Domain.Models.Player player = new()
+	{
+		Name = "test"
+	};
+
+	protected async Task SavePlayer()
+	{
+		var response = await httpClient.PostAsJsonAsync("api/players", player);
+		response.EnsureSuccessStatusCode();
+	}
+
+	protected void Cancel()
+	{
+		NavigationManager.NavigateTo("/players");
+	}
+}

```

#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/Program.cs
*Summary:* Added player list page

**C# format check:**
```
```
**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/Program.cs b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/Program.cs
index 91db88a..45fddd3 100644
--- a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/Program.cs
+++ b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.Client/Program.cs
@@ -2,4 +2,6 @@ using Microsoft.AspNetCore.Components.WebAssembly.Hosting;
 
 var builder = WebAssemblyHostBuilder.CreateDefault(args);
 
+builder.Services.AddScoped(s => new HttpClient { BaseAddress = new Uri(builder.HostEnvironment.BaseAddress) });
+
 await builder.Build().RunAsync();
\ No newline at end of file

```

#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.csproj
*Summary:* Added player API controller and Create endpoint

**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.csproj b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.csproj
index af238c2..57062b8 100644
--- a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.csproj
+++ b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor.csproj
@@ -12,10 +12,15 @@
           <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
         </PackageReference>
         <PackageReference Include="Microsoft.EntityFrameworkCore.Relational" Version="8.0.12" />
+        <PackageReference Include="Microsoft.EntityFrameworkCore.Tools" Version="8.0.11">
+          <PrivateAssets>all</PrivateAssets>
+          <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
+        </PackageReference>
+        <PackageReference Include="Microsoft.VisualStudio.Web.CodeGeneration.Design" Version="8.0.7" />
         <ProjectReference Include="..\..\BowlingTrackerSupreme.Infrastructure\BowlingTrackerSupreme.Infrastructure.csproj" />
         <ProjectReference Include="..\..\BowlingTrackerSupreme.Migrations\BowlingTrackerSupreme.Migrations.csproj" />
-        <ProjectReference Include="..\BowlingTrackerSupreme.Blazor.Client\BowlingTrackerSupreme.Blazor.Client.csproj"/>
-        <PackageReference Include="Microsoft.AspNetCore.Components.WebAssembly.Server" Version="8.0.11"/>
+        <ProjectReference Include="..\BowlingTrackerSupreme.Blazor.Client\BowlingTrackerSupreme.Blazor.Client.csproj" />
+        <PackageReference Include="Microsoft.AspNetCore.Components.WebAssembly.Server" Version="8.0.11" />
     </ItemGroup>
 
 </Project>

```

#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/App.razor
*Summary:* Replaced header 'About' with bowling XiaoPang

**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/App.razor b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/App.razor
index b472916..070d0f6 100644
--- a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/App.razor
+++ b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/App.razor
@@ -8,7 +8,7 @@
     <link rel="stylesheet" href="bootstrap/bootstrap.min.css"/>
     <link rel="stylesheet" href="app.css"/>
     <link rel="stylesheet" href="BowlingTrackerSupreme.Blazor.styles.css"/>
-    <link rel="icon" type="image/png" href="favicon.png"/>
+    <link rel="icon" type="image/png" href="images/favicon.png"/>
     <HeadOutlet/>
 </head>
 

```

#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Layout/MainLayout.razor
*Summary:* Replaced header 'About' with bowling XiaoPang

**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Layout/MainLayout.razor b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Layout/MainLayout.razor
index df0c2d6..ef5f464 100644
--- a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Layout/MainLayout.razor
+++ b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Layout/MainLayout.razor
@@ -7,7 +7,7 @@
 
     <main>
         <div class="top-row px-4">
-            <a href="https://learn.microsoft.com/aspnet/core/" target="_blank">About</a>
+            <img src="images/favicon.png" style="height: 50px; width: 50px;" />
         </div>
 
         <article class="content px-4">

```

#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Layout/NavMenu.razor
*Summary:* Added player list page

**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Layout/NavMenu.razor b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Layout/NavMenu.razor
index 2ccfe05..bb8d17e 100644
--- a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Layout/NavMenu.razor
+++ b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Layout/NavMenu.razor
@@ -14,9 +14,15 @@
             </NavLink>
         </div>
 
+        <div class="nav-item px-3">
+            <NavLink class="nav-link" href="players">
+                <span class="bi bi-list-nested-nav-menu" aria-hidden="true"></span> Players
+            </NavLink>
+        </div>
+
         <div class="nav-item px-3">
             <NavLink class="nav-link" href="games">
-                <span class="bi bi-plus-square-fill-nav-menu" aria-hidden="true"></span> Games
+                <span class="bi bi-house-door-fill-nav-menu bi-plus-square-fill-nav-menu" aria-hidden="true"></span> Games
             </NavLink>
         </div>
 

```

#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Game.razor
*Summary:* WIP: Game and player view

**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Game.razor b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Game.razor
new file mode 100644
index 0000000..6b754bf
--- /dev/null
+++ b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Game.razor
@@ -0,0 +1,127 @@
+﻿@page "/game/{Id}"
+@using BowlingTrackerSupreme.Domain.Models
+@using BowlingTrackerSupreme.Infrastructure.Database
+@inject BowlingTrackerSupremeDbContext DbContext
+@inject NavigationManager NavigationManager
+@attribute [StreamRendering]
+
+<PageTitle>Game - @_game?.PlayedOn</PageTitle>
+<h3>Game - 
+	@if (_game == null) { <em>Loading...</em>}
+    else { @_game.PlayedOn }
+</h3>
+
+<table class="table table-striped table-hover table-responsive">
+    <caption>Game players: 
+        @if (_players == null) { <em>Loading...</em> }
+        else { _players.Count(); }
+    </caption>
+    <thead>
+        <tr class="d-flex flex-nowrap flex-row">
+            <th class="d-flex justify-content-start w-50" >Player</th>
+            @for(var index = 1; index <= 10; index++)
+            {
+                <th class="d-flex flex-nowrap justify-content-center" style="width: 100px;" >@index</th>
+            }
+            <th class="d-flex justify-content-center w-50">Score</th>
+        </tr>
+    </thead>
+    <tbody>
+        @if (_playerGames != null)
+        {
+            @foreach (var playerGame in _playerGames)
+            {
+                <tr class="d-flex">
+                    <td class="d-flex align-content-center w-50" >@playerGame.Player.Name</td>
+                    @foreach(var frame in playerGame.Frames)
+                    {
+                        <td style="width: 100px;">
+                            <div class="d-flex flex-md-wrap border-1">
+                                <div class="d-flex justify-content-center w-50">
+                                    @frame.FirstRoll?.PinsHit
+                                </div>
+                                <div class="d-flex justify-content-center w-50 border border-1 border-dark">
+                                    @if(frame.IsSpare) { <div>/</div> }
+                                    else { @frame.SecondRoll?.PinsHit }
+                                </div>
+                                <div class="w-100 d-flex justify-content-center">
+                                   <b>@frame.Score</b>
+                                </div>
+                            </div>	
+                        </td>
+                    }
+                    <td class="d-flex w-50">300</td>
+                </tr>
+            }
+        }
+    </tbody>
+</table>
+
+@code {
+    [Parameter]
+    public string Id { get; set; }
+
+    private Domain.Models.Game _game;
+    private IEnumerable<Domain.Models.Frame> _frames;
+    private IEnumerable<Domain.Models.PlayerGame> _playerGames;
+    private IEnumerable<Domain.Models.Player> _players;
+
+    protected override async Task OnInitializedAsync()
+    {
+        if (!Guid.TryParse(Id, out var gameId))
+        {
+            NavigationManager.NavigateTo("/error");
+        }
+        var game = await DbContext.Games.FindAsync(gameId);
+        if (game == null)
+        {
+            NavigationManager.NavigateTo("/error");
+        }
+
+        _playerGames = new List<PlayerGame>
+        {
+            new PlayerGame
+            {
+                Id = Guid.NewGuid(),
+                GameId = game.Id,
+                Player = new Domain.Models.Player
+                {
+                    Id = Guid.NewGuid(),
+                    Name = "Butterfly"
+                },
+                Game = game,
+                PlayerId = Guid.NewGuid(),
+                Frames = new List<Frame>
+                {
+                    new Frame
+                    {
+                        Id = Guid.NewGuid(),
+                        FirstRoll = new Roll
+                        {
+                            PinsHit = 9,
+                        },
+                        SecondRoll = new Roll
+                        {
+                            PinsHit = 1,
+                        },
+                        Score = 20
+                    },
+                    new Frame(),
+                    new Frame(),
+                    new Frame(),
+                    new Frame(),
+                    new Frame(),
+                    new Frame(),
+                    new Frame(),
+                    new Frame(),
+                    new Frame(),
+                }
+            }
+        };
+        // var playerGames = DbContext.PlayerGames.First();
+		// var playerIds = _playerGames.Select(p => p.PlayerId).ToList();
+		// _players = DbContext.Players.Where(x => playerIds.Contains(x.Id)).ToList();
+
+		_game = game;
+	}
+}

```

#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Games.razor
*Summary:* WIP: Game and player view

**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Games.razor b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Games.razor
new file mode 100644
index 0000000..883b74e
--- /dev/null
+++ b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Games.razor
@@ -0,0 +1,56 @@
+@page "/games"
+@using BowlingTrackerSupreme.Domain.Models
+@using BowlingTrackerSupreme.Infrastructure.Database
+@using Microsoft.EntityFrameworkCore
+@inject BowlingTrackerSupremeDbContext DbContext
+@attribute [StreamRendering]
+
+<PageTitle>Games</PageTitle>
+
+<h1>50 most recent games:</h1>
+
+@if (_games == null) { <em>Loading...</em> }
+else
+{
+    <table class="table">
+        <thead>
+			<tr>
+				<th>Played On</th>
+                <th class="text-nowrap">Winning player</th>
+				<th class="text-nowrap">Created On</th>
+				<th class="text-nowrap">Modified On</th>
+			</tr>
+        </thead>
+        <tbody>
+        @foreach (var game in _games)
+        {
+            <tr>
+                <td class="w-100"><a href="game/@game.Id">@game.PlayedOn</a></td>
+                <td class="text-nowrap"><a href="player/@game.WinningPlayerId">@game.WinningPlayer?.Name</a></td>
+                <td class="text-end text-nowrap">@game.CreatedOn</td>
+                <td class="text-end text-nowrap">@game.ModifiedOn</td>
+            </tr>
+        }
+        </tbody>
+    </table>
+}
+
+@code
+{
+    private IEnumerable<Domain.Models.Game>? _games;
+
+    protected override async Task OnInitializedAsync()
+    {
+        _games = await DbContext.Games
+            .Take(50)
+            .OrderByDescending(g => g.CreatedOn)
+            .Select(g => new Domain.Models.Game
+            {
+                Id = g.Id,
+                CreatedOn = g.CreatedOn,
+                ModifiedOn = g.ModifiedOn,
+                WinningPlayer = g.WinningPlayer
+            })
+            .ToListAsync();
+    }
+}

```

#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Home.razor
*Summary:* Updated homepage

**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Home.razor b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Home.razor
index dfcdf75..b7ed324 100644
--- a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Home.razor
+++ b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Home.razor
@@ -1,7 +1,46 @@
 ﻿@page "/"
+@using BowlingTrackerSupreme.Infrastructure.Database
+@inject BowlingTrackerSupremeDbContext DbContext
+@attribute [StreamRendering]
 
 <PageTitle>Home</PageTitle>
+<div class="mb-4">
+	<h1>Hello, world!</h1>
 
-<h1>Hello, world!</h1>
+	Welcome to the Bowling Tracker Supreme app.
+</div>
+<div>
+	<p><strong>Players: </strong>
+		@if (PlayerCount == null) { <em>Loading...</em> }
+		else { @PlayerCount }
+	</p>
+	<p><strong>Player Names: </strong>
+		@if (PlayerNamesCount == null) { <em>Loading...</em> }
+		else { @PlayerNamesCount }
+	</p>
+	<p><strong>Games: </strong>
+		@if (GamesCount== null) { <em>Loading...</em> }
+		else { @GamesCount}
+	</p>
+	<p><strong>Frames: </strong>
+		@if (FramesCount == null) { <em>Loading...</em> }
+		else { @FramesCount }
+	</p>
+</div>
 
-Welcome to your new app.
\ No newline at end of file
+@code
+{
+	private int? PlayerCount;
+	private int? PlayerNamesCount;
+	private int? GamesCount;
+	private int? FramesCount;
+
+	protected override async Task OnInitializedAsync()
+	{
+		await base.OnInitializedAsync();
+
+		PlayerCount = DbContext.Players.Count();
+		GamesCount = DbContext.Games.Count();
+		FramesCount = DbContext.Frames.Count();
+	}
+}
\ No newline at end of file

```

#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Player.razor
*Summary:* WIP: Game and player view

**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Player.razor b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Player.razor
new file mode 100644
index 0000000..516b483
--- /dev/null
+++ b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Player.razor
@@ -0,0 +1,29 @@
+﻿@page "/player/{Id}"
+@using BowlingTrackerSupreme.Infrastructure.Database;
+@inject BowlingTrackerSupremeDbContext DbContext;
+@inject NavigationManager NavigationManager;
+@attribute [StreamRendering]
+
+<PageTitle>Player</PageTitle>
+<h3>
+	@if(_player == null) { <em>Loading...</em> }
+	else { @_player.Name }
+</h3>
+
+@code {
+	[Parameter]
+	public string Id { get; set; }
+
+	private Domain.Models.Player _player;
+
+	protected override async Task OnInitializedAsync()
+	{
+		if (!Guid.TryParse(Id, out var id))
+		{
+			NavigationManager.NavigateTo("/error");
+		}
+
+		_player = await DbContext.Players.FindAsync(id);
+
+	}
+}

```

#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Players.razor
*Summary:* WIP: Game and player view

**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Players.razor b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Players.razor
new file mode 100644
index 0000000..9609b44
--- /dev/null
+++ b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Players.razor
@@ -0,0 +1,50 @@
+﻿@page "/players"
+@using BowlingTrackerSupreme.Domain.Models
+@using BowlingTrackerSupreme.Infrastructure.Database
+@inject BowlingTrackerSupremeDbContext DbContext
+@attribute [StreamRendering]
+
+<PageTitle>Players</PageTitle>
+
+<div class="d-flex justify-content-between">
+	<h3>Players</h3>
+	<a href="player" class="btn btn-info" style="min-width: 100px;">New</a>
+</div>
+
+@if (PlayerList == null) { <em>Loading...</em> }
+else
+{
+	<table class="table table-striped table-hover table-responsive">
+		<caption>List of players: @PlayerList.Count()</caption>
+		<thead> 
+			<tr>
+				<th scope="col" class="w-100">Name</th>
+				<th scope="col" class="text-end text-nowrap">Created On</th>
+				<th scope="col" class="text-end text-nowrap">Modified On</th>
+			</tr>
+		</thead>
+		<tbody>
+			@foreach(var player in PlayerList)
+			{
+				<tr >
+					<td class="w-100"><a href="player/@player.Id">@player.Name</a></td>
+					<td class="text-end text-nowrap">@player.CreatedOn</td>
+					<td class="text-end text-nowrap">@player.ModifiedOn</td>
+				</tr>
+			}
+		</tbody>
+
+	</table>
+}
+
+
+@code {
+	protected IEnumerable<Domain.Models.Player> PlayerList;
+
+	protected override async Task OnInitializedAsync()
+	{
+		PlayerList = (from p in DbContext.Players
+			orderby p.CreatedOn descending
+							select p).ToList();
+	}
+}

```

#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Test.razor
*Summary:* Added Games controller

**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Test.razor b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Test.razor
deleted file mode 100644
index 4f8cc72..0000000
--- a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Components/Pages/Test.razor
+++ /dev/null
@@ -1,64 +0,0 @@
-@page "/games"
-@using BowlingTrackerSupreme.Domain.Models
-@using BowlingTrackerSupreme.Infrastructure.Database
-@using Microsoft.EntityFrameworkCore
-@inject BowlingTrackerSupremeDbContext DbContext
-@rendermode InteractiveAuto
-
-<PageTitle>Games</PageTitle>
-
-<h1>50 most recent games:</h1>
-
-@if (_games == null)
-{
-    <p>
-        <em>Loading...</em>
-    </p>
-}
-else
-{
-    <table class="table">
-        <thead>
-        <tr>
-            <th>ParticipantCount</th>
-            <th>Date created</th>
-            <th>Date played</th>
-        </tr>
-        </thead>
-        <tbody>
-        @foreach (var game in _games)
-        {
-            <tr>
-                <td>@game.ParticipantCount</td>
-                <td>@game.DateCreated.ToShortDateString()</td>
-                <td>@game.DatePlayed.ToShortDateString()</td>
-            </tr>
-        }
-        </tbody>
-    </table>
-}
-
-@code
-{
-    private DisplayGame[]? _games;
-
-    protected override async Task OnInitializedAsync()
-    {
-        _games = await DbContext.Games
-            .Take(50)
-            .Select(g => new DisplayGame
-            {
-                DateCreated = g.DateCreated,
-                DatePlayed = g.DatePlayed,
-                ParticipantCount = g.Participants.Count(),
-            })
-            .ToArrayAsync();
-    }
-
-    private class DisplayGame
-    {
-        public int ParticipantCount { get; set; }
-        public DateTime DatePlayed { get; set; }
-        public DateTime DateCreated { get; set; }
-    }
-}

```

#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Controllers/GamesController.cs
*Summary:* WIP: Game and player view

**C# format check:**
```
```
**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Controllers/GamesController.cs b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Controllers/GamesController.cs
new file mode 100644
index 0000000..4bb1a61
--- /dev/null
+++ b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Controllers/GamesController.cs
@@ -0,0 +1,52 @@
+﻿using BowlingTrackerSupreme.Domain.Models;
+using BowlingTrackerSupreme.Infrastructure.Database;
+using Microsoft.AspNetCore.Mvc;
+using Microsoft.EntityFrameworkCore;
+using System.ComponentModel.DataAnnotations;
+
+namespace BowlingTrackerSupreme.Blazor.Controllers
+{
+    [Route("api/[controller]")]
+    [ApiController]
+    public class GamesController : ControllerBase
+    {
+        private readonly BowlingTrackerSupremeDbContext _context;
+
+        public GamesController(BowlingTrackerSupremeDbContext context)
+        {
+            _context = context;
+        }
+
+        [HttpGet]
+        public async Task<IActionResult> Get()
+        {
+            var games = await _context.Games.ToListAsync();
+
+            return new OkObjectResult(games);
+        }
+
+        [HttpPost]
+        public async Task<IActionResult> Create([FromBody][Required] Game game)
+        {
+            if (game.Id.HasValue) game.Id = null;
+            if (game.CreatedOn.HasValue) game.CreatedOn = null;
+            if (game.ModifiedOn.HasValue) game.ModifiedOn = null;
+
+            var player = await _context.Players.FindAsync(game.WinningPlayer?.Id);
+            if (player == null)
+            {
+                return new BadRequestObjectResult($"{nameof(game.WinningPlayer)} not found: {game.WinningPlayer?.Id}");
+            }
+
+            game.WinningPlayer = player;
+            game.WinningPlayerId = player.Id;
+
+            await _context.AddAsync(game);
+            await _context.SaveChangesAsync();
+
+            var insertedGame = await _context.Games.FindAsync(game.Id);
+
+            return new OkObjectResult(insertedGame);
+        }
+    }
+}

```

#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Controllers/PlayersController.cs
*Summary:* Added player API controller and Create endpoint

**C# format check:**
```
```
**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Controllers/PlayersController.cs b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Controllers/PlayersController.cs
new file mode 100644
index 0000000..757e1d1
--- /dev/null
+++ b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Controllers/PlayersController.cs
@@ -0,0 +1,43 @@
+﻿using BowlingTrackerSupreme.Domain.Models;
+using BowlingTrackerSupreme.Infrastructure.Database;
+using Microsoft.AspNetCore.Mvc;
+using Microsoft.EntityFrameworkCore;
+using Newtonsoft.Json;
+using System.ComponentModel.DataAnnotations;
+
+namespace BowlingTrackerSupreme.Blazor.Controllers
+{
+    [Route("api/[controller]")]
+    [ApiController]
+    public class PlayersController : ControllerBase
+    {
+        private readonly BowlingTrackerSupremeDbContext _context;
+
+        public PlayersController(BowlingTrackerSupremeDbContext context)
+        {
+            _context = context;
+        }
+
+        [HttpGet]
+        public async Task<IActionResult> Get()
+        {
+            var players = await _context.Players.ToListAsync();
+
+            return new OkObjectResult(players);
+        }
+
+        [HttpPost]
+        public async Task<IActionResult> Create([FromBody][Required] Player player)
+        {
+            if (player.Id.HasValue)         player.Id = null;
+            if (player.CreatedOn.HasValue)  player.CreatedOn = null;
+            if (player.ModifiedOn.HasValue) player.ModifiedOn = null;
+
+            await _context.AddAsync(player);
+            await _context.SaveChangesAsync();
+
+            var insertedPlayer = await _context.Players.FindAsync(player.Id);
+            return new OkObjectResult(insertedPlayer);
+        }
+    }
+}

```

#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Program.cs
*Summary:* Added player API controller and Create endpoint

**C# format check:**
```
```
**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Program.cs b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Program.cs
index 2499f44..4f0bc8d 100644
--- a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Program.cs
+++ b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/Program.cs
@@ -9,7 +9,6 @@ builder.Services.AddRazorComponents()
     .AddInteractiveServerComponents()
     .AddInteractiveWebAssemblyComponents();
 
-
 builder.Services.AddBowlingTrackerSupremeInfrastructure(builder.Configuration, contextOptionsBuilder =>
 {
     contextOptionsBuilder.AllowMigrationManagement();
@@ -22,6 +21,8 @@ builder.Services.AddHsts(options =>
     options.MaxAge = TimeSpan.FromDays(7);
 });
 
+builder.Services.AddControllers();
+
 var app = builder.Build();
 
 // Configure the HTTP request pipeline.
@@ -37,6 +38,8 @@ else
 }
 
 app.UseHttpsRedirection();
+app.UseRouting();
+app.MapControllers();
 
 app.UseStaticFiles();
 app.UseAntiforgery();

```

#### File: src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/wwwroot/images/favicon.png
*Summary:* Replaced header 'About' with bowling XiaoPang

**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/wwwroot/images/favicon.png b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/wwwroot/images/favicon.png
new file mode 100644
index 0000000..9886442
Binary files /dev/null and b/src/BowlingTrackerSupreme.Blazor/BowlingTrackerSupreme.Blazor/wwwroot/images/favicon.png differ

```

#### File: src/BowlingTrackerSupreme.Domain/Models/Frame.cs
*Summary:* Added CreatedOn and ModifiedOn to entities

**C# format check:**
```
```
**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Domain/Models/Frame.cs b/src/BowlingTrackerSupreme.Domain/Models/Frame.cs
index e8563c1..28224b3 100644
--- a/src/BowlingTrackerSupreme.Domain/Models/Frame.cs
+++ b/src/BowlingTrackerSupreme.Domain/Models/Frame.cs
@@ -3,6 +3,8 @@ namespace BowlingTrackerSupreme.Domain.Models;
 public class Frame
 {
     public Guid Id { get; set; }
+    public DateTime CreatedOn { get; set; }
+    public DateTime ModifiedOn { get; set; }
     public Guid PlayerGameId { get; set; }
     public PlayerGame PlayerGame { get; set; } = null!;
     

```

#### File: src/BowlingTrackerSupreme.Domain/Models/Game.cs
*Summary:* Added Games controller

**C# format check:**
```
```
**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Domain/Models/Game.cs b/src/BowlingTrackerSupreme.Domain/Models/Game.cs
index a97cd8f..26b185c 100644
--- a/src/BowlingTrackerSupreme.Domain/Models/Game.cs
+++ b/src/BowlingTrackerSupreme.Domain/Models/Game.cs
@@ -2,11 +2,12 @@ namespace BowlingTrackerSupreme.Domain.Models;
 
 public class Game
 {
-    public Guid Id { get; set; }
-    public Player WinningPlayer { get; set; } = null!;
-    public Guid WinningPlayerId { get; set; }
-    public DateTime DateCreated { get; set; }
-    public DateTime DatePlayed { get; set; }
+    public Guid? Id { get; set; }
+    public DateTime? CreatedOn { get; set; }
+    public DateTime? ModifiedOn { get; set; }
+    public DateTime PlayedOn { get; set; }
+    public Player? WinningPlayer { get; set; } = null!;
+    public Guid? WinningPlayerId { get; set; }
     public IEnumerable<PlayerGame> PlayerGames { get; set; } = [];
     public IEnumerable<Player> Participants { get; set; } = [];
 }
\ No newline at end of file

```

#### File: src/BowlingTrackerSupreme.Domain/Models/Player.cs
*Summary:* Added Games controller

**C# format check:**
```
```
**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Domain/Models/Player.cs b/src/BowlingTrackerSupreme.Domain/Models/Player.cs
index 5ec82b6..4b5d77b 100644
--- a/src/BowlingTrackerSupreme.Domain/Models/Player.cs
+++ b/src/BowlingTrackerSupreme.Domain/Models/Player.cs
@@ -1,9 +1,15 @@
-﻿namespace BowlingTrackerSupreme.Domain.Models;
+﻿using System.ComponentModel;
+using System.Runtime.Serialization;
+
+namespace BowlingTrackerSupreme.Domain.Models;
 
 public class Player
 {
-    public Guid Id { get; set; }
-    public required string Name { get; set; }
+    public Guid? Id { get; set; }
+    public string? Name { get; set; }
+    public DateTime? CreatedOn { get; set; }
+    public DateTime? ModifiedOn { get; set; }
+
     public IEnumerable<Game> GameParticipation { get; set; } = [];
     public IEnumerable<PlayerGame> PlayedGames { get; set; } = [];
 }
\ No newline at end of file

```

#### File: src/BowlingTrackerSupreme.Domain/Models/PlayerGame.cs
*Summary:* WIP: Game and player view

**C# format check:**
```
```
**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Domain/Models/PlayerGame.cs b/src/BowlingTrackerSupreme.Domain/Models/PlayerGame.cs
index 81181b5..47d6769 100644
--- a/src/BowlingTrackerSupreme.Domain/Models/PlayerGame.cs
+++ b/src/BowlingTrackerSupreme.Domain/Models/PlayerGame.cs
@@ -2,10 +2,12 @@ namespace BowlingTrackerSupreme.Domain.Models;
 
 public class PlayerGame
 {
-    public Guid Id { get; set; }
-    public Guid PlayerId { get; set; }
+    public Guid? Id { get; set; }
+    public DateTime? CreatedOn { get; set; }
+    public DateTime? ModifiedOn { get; set; }
+    public Guid? PlayerId { get; set; }
     public Player Player { get; set; } = null!;
-    public Guid GameId { get; set; }
+    public Guid? GameId { get; set; }
     public Game Game { get; set; } = null!;
-    public IEnumerable<Frame> Frames { get; set; } = [];
+    public IEnumerable<Frame> Frames { get; set; }
 }
\ No newline at end of file

```

#### File: src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/FrameConfiguration.cs
*Summary:* Added CreatedOn and ModifiedOn to entities

**C# format check:**
```
```
**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/FrameConfiguration.cs b/src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/FrameConfiguration.cs
index 476c20f..1c1c0a5 100644
--- a/src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/FrameConfiguration.cs
+++ b/src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/FrameConfiguration.cs
@@ -9,6 +9,12 @@ public class FrameConfiguration : IEntityTypeConfiguration<Frame>
     public void Configure(EntityTypeBuilder<Frame> builder)
     {
         builder.HasKey(x => x.Id);
+        builder.Property(f => f.CreatedOn)
+            .ValueGeneratedOnAdd()
+            .HasDefaultValueSql("timezone('utc', now())");
+        builder.Property(f => f.ModifiedOn)
+            .ValueGeneratedOnAddOrUpdate()
+            .HasDefaultValueSql("timezone('utc', now())");
         builder.OwnsOne(x => x.FirstRoll);
         builder.OwnsOne(x => x.SecondRoll);
         builder.Ignore(x => x.AllRolls);

```

#### File: src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/GameConfiguration.cs
*Summary:* Added CreatedOn and ModifiedOn to entities

**C# format check:**
```
```
**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/GameConfiguration.cs b/src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/GameConfiguration.cs
index 4cc1021..ef65adf 100644
--- a/src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/GameConfiguration.cs
+++ b/src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/GameConfiguration.cs
@@ -9,6 +9,12 @@ public class GameConfiguration : IEntityTypeConfiguration<Game>
     public void Configure(EntityTypeBuilder<Game> builder)
     {
         builder.HasKey(x => x.Id);
+        builder.Property(g => g.CreatedOn)
+            .ValueGeneratedOnAdd()
+            .HasDefaultValueSql("timezone('utc', now())");
+        builder.Property(g => g.ModifiedOn)
+            .ValueGeneratedOnAddOrUpdate()
+            .HasDefaultValueSql("timezone('utc', now())");
         builder.HasMany<Player>(x => x.Participants)
             .WithMany(x => x.GameParticipation);
         builder.HasOne(x => x.WinningPlayer)

```

#### File: src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/PlayerConfiguration.cs
*Summary:* Added CreatedOn and ModifiedOn to entities

**C# format check:**
```
```
**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/PlayerConfiguration.cs b/src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/PlayerConfiguration.cs
index 93633c6..12a0e32 100644
--- a/src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/PlayerConfiguration.cs
+++ b/src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/PlayerConfiguration.cs
@@ -9,9 +9,14 @@ public class PlayerConfiguration : IEntityTypeConfiguration<Player>
     public void Configure(EntityTypeBuilder<Player> builder)
     {
         builder.HasKey(x => x.Id);
+        builder.Property(p => p.CreatedOn)
+            .ValueGeneratedOnAdd()
+            .HasDefaultValueSql("timezone('utc', now())");
+        builder.Property(p => p.ModifiedOn)
+            .ValueGeneratedOnAddOrUpdate()
+            .HasDefaultValueSql("timezone('utc', now())");
         builder.HasMany(x => x.PlayedGames)
             .WithOne(x => x.Player)
             .HasForeignKey(x => x.PlayerId);
-        
     }
 }
\ No newline at end of file

```

#### File: src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/PlayerGameConfiguration.cs
*Summary:* Added CreatedOn and ModifiedOn to entities

**C# format check:**
```
```
**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/PlayerGameConfiguration.cs b/src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/PlayerGameConfiguration.cs
index 2315f11..e9fea31 100644
--- a/src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/PlayerGameConfiguration.cs
+++ b/src/BowlingTrackerSupreme.Infrastructure/Database/EntityConfigurations/PlayerGameConfiguration.cs
@@ -9,6 +9,12 @@ public class PlayerGameConfiguration : IEntityTypeConfiguration<PlayerGame>
     public void Configure(EntityTypeBuilder<PlayerGame> builder)
     {
         builder.HasKey(x => x.Id);
+        builder.Property(p => p.CreatedOn)
+            .ValueGeneratedOnAdd()
+            .HasDefaultValueSql("timezone('utc', now())");
+        builder.Property(p => p.ModifiedOn)
+            .ValueGeneratedOnAddOrUpdate()
+            .HasDefaultValueSql("timezone('utc', now())");
         builder.HasMany(x => x.Frames)
             .WithOne(x => x.PlayerGame)
             .HasForeignKey(x => x.PlayerGameId);

```

#### File: src/BowlingTrackerSupreme.Migrations/Migrations/20250225212756_AddedCreatedOnModifiedOn.Designer.cs
*Summary:* Added CreatedOn and ModifiedOn to entities

**C# format check:**
```
```
**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Migrations/Migrations/20250225212756_AddedCreatedOnModifiedOn.Designer.cs b/src/BowlingTrackerSupreme.Migrations/Migrations/20250225212756_AddedCreatedOnModifiedOn.Designer.cs
new file mode 100644
index 0000000..14da28d
--- /dev/null
+++ b/src/BowlingTrackerSupreme.Migrations/Migrations/20250225212756_AddedCreatedOnModifiedOn.Designer.cs
@@ -0,0 +1,313 @@
+﻿// <auto-generated />
+using System;
+using BowlingTrackerSupreme.Infrastructure.Database;
+using Microsoft.EntityFrameworkCore;
+using Microsoft.EntityFrameworkCore.Infrastructure;
+using Microsoft.EntityFrameworkCore.Migrations;
+using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
+using Npgsql.EntityFrameworkCore.PostgreSQL.Metadata;
+
+#nullable disable
+
+namespace BowlingTrackerSupreme.Migrations.Migrations
+{
+    [DbContext(typeof(BowlingTrackerSupremeDbContext))]
+    [Migration("20250225212756_AddedCreatedOnModifiedOn")]
+    partial class AddedCreatedOnModifiedOn
+    {
+        /// <inheritdoc />
+        protected override void BuildTargetModel(ModelBuilder modelBuilder)
+        {
+#pragma warning disable 612, 618
+            modelBuilder
+                .HasAnnotation("ProductVersion", "8.0.12")
+                .HasAnnotation("Relational:MaxIdentifierLength", 63);
+
+            NpgsqlModelBuilderExtensions.UseIdentityByDefaultColumns(modelBuilder);
+
+            modelBuilder.Entity("BowlingTrackerSupreme.Domain.Models.Frame", b =>
+                {
+                    b.Property<Guid>("Id")
+                        .ValueGeneratedOnAdd()
+                        .HasColumnType("uuid");
+
+                    b.Property<DateTime>("CreatedOn")
+                        .ValueGeneratedOnAdd()
+                        .HasColumnType("timestamp with time zone")
+                        .HasDefaultValueSql("timezone('utc', now())");
+
+                    b.Property<string>("Discriminator")
+                        .IsRequired()
+                        .HasMaxLength(13)
+                        .HasColumnType("character varying(13)");
+
+                    b.Property<Guid>("FirstRollId")
+                        .HasColumnType("uuid");
+
+                    b.Property<int>("FrameNumber")
+                        .HasColumnType("integer");
+
+                    b.Property<DateTime>("ModifiedOn")
+                        .ValueGeneratedOnAddOrUpdate()
+                        .HasColumnType("timestamp with time zone")
+                        .HasDefaultValueSql("timezone('utc', now())");
+
+                    b.Property<Guid>("PlayerGameId")
+                        .HasColumnType("uuid");
+
+                    b.Property<int?>("Score")
+                        .HasColumnType("integer");
+
+                    b.Property<Guid>("SecondRollId")
+                        .HasColumnType("uuid");
+
+                    b.HasKey("Id");
+
+                    b.HasIndex("PlayerGameId");
+
+                    b.ToTable("Frames");
+
+                    b.HasDiscriminator().HasValue("Frame");
+
+                    b.UseTphMappingStrategy();
+                });
+
+            modelBuilder.Entity("BowlingTrackerSupreme.Domain.Models.Game", b =>
+                {
+                    b.Property<Guid>("Id")
+                        .ValueGeneratedOnAdd()
+                        .HasColumnType("uuid");
+
+                    b.Property<DateTime>("CreatedOn")
+                        .ValueGeneratedOnAdd()
+                        .HasColumnType("timestamp with time zone")
+                        .HasDefaultValueSql("timezone('utc', now())");
+
+                    b.Property<DateTime>("ModifiedOn")
+                        .ValueGeneratedOnAddOrUpdate()
+                        .HasColumnType("timestamp with time zone")
+                        .HasDefaultValueSql("timezone('utc', now())");
+
+                    b.Property<DateTime>("PlayedOn")
+                        .HasColumnType("timestamp with time zone");
+
+                    b.Property<Guid>("WinningPlayerId")
+                        .HasColumnType("uuid");
+
+                    b.HasKey("Id");
+
+                    b.HasIndex("WinningPlayerId");
+
+                    b.ToTable("Games");
+                });
+
+            modelBuilder.Entity("BowlingTrackerSupreme.Domain.Models.Player", b =>
+                {
+                    b.Property<Guid>("Id")
+                        .ValueGeneratedOnAdd()
+                        .HasColumnType("uuid");
+
+                    b.Property<DateTime>("CreatedOn")
+                        .ValueGeneratedOnAdd()
+                        .HasColumnType("timestamp with time zone")
+                        .HasDefaultValueSql("timezone('utc', now())");
+
+                    b.Property<DateTime>("ModifiedOn")
+                        .ValueGeneratedOnAddOrUpdate()
+                        .HasColumnType("timestamp with time zone")
+                        .HasDefaultValueSql("timezone('utc', no
```
_Chunk 2_
```
w())");
+
+                    b.Property<string>("Name")
+                        .IsRequired()
+                        .HasColumnType("text");
+
+                    b.HasKey("Id");
+
+                    b.ToTable("Players");
+                });
+
+            modelBuilder.Entity("BowlingTrackerSupreme.Domain.Models.PlayerGame", b =>
+                {
+                    b.Property<Guid>("Id")
+                        .ValueGeneratedOnAdd()
+                        .HasColumnType("uuid");
+
+                    b.Property<DateTime>("CreatedOn")
+                        .ValueGeneratedOnAdd()
+                        .HasColumnType("timestamp with time zone")
+                        .HasDefaultValueSql("timezone('utc', now())");
+
+                    b.Property<Guid>("GameId")
+                        .HasColumnType("uuid");
+
+                    b.Property<DateTime>("ModifiedOn")
+                        .ValueGeneratedOnAddOrUpdate()
+                        .HasColumnType("timestamp with time zone")
+                        .HasDefaultValueSql("timezone('utc', now())");
+
+                    b.Property<Guid>("PlayerId")
+                        .HasColumnType("uuid");
+
+                    b.HasKey("Id");
+
+                    b.HasIndex("GameId");
+
+                    b.HasIndex("PlayerId");
+
+                    b.ToTable("PlayerGames");
+                });
+
+            modelBuilder.Entity("GamePlayer", b =>
+                {
+                    b.Property<Guid>("GameParticipationId")
+                        .HasColumnType("uuid");
+
+                    b.Property<Guid>("ParticipantsId")
+                        .HasColumnType("uuid");
+
+                    b.HasKey("GameParticipationId", "ParticipantsId");
+
+                    b.HasIndex("ParticipantsId");
+
+                    b.ToTable("GamePlayer");
+                });
+
+            modelBuilder.Entity("BowlingTrackerSupreme.Domain.Models.FinalFrame", b =>
+                {
+                    b.HasBaseType("BowlingTrackerSupreme.Domain.Models.Frame");
+
+                    b.HasDiscriminator().HasValue("FinalFrame");
+                });
+
+            modelBuilder.Entity("BowlingTrackerSupreme.Domain.Models.Frame", b =>
+                {
+                    b.HasOne("BowlingTrackerSupreme.Domain.Models.PlayerGame", "PlayerGame")
+                        .WithMany("Frames")
+                        .HasForeignKey("PlayerGameId")
+                        .OnDelete(DeleteBehavior.Cascade)
+                        .IsRequired();
+
+                    b.OwnsOne("BowlingTrackerSupreme.Domain.Models.Roll", "FirstRoll", b1 =>
+                        {
+                            b1.Property<Guid>("FrameId")
+                                .HasColumnType("uuid");
+
+                            b1.Property<int>("PinsHit")
+                                .HasColumnType("integer");
+
+                            b1.HasKey("FrameId");
+
+                            b1.ToTable("Frames");
+
+                            b1.WithOwner()
+                                .HasForeignKey("FrameId");
+                        });
+
+                    b.OwnsOne("BowlingTrackerSupreme.Domain.Models.Roll", "SecondRoll", b1 =>
+                        {
+                            b1.Property<Guid>("FrameId")
+                                .HasColumnType("uuid");
+
+                            b1.Property<int>("PinsHit")
+                                .HasColumnType("integer");
+
+                            b1.HasKey("FrameId");
+
+                            b1.ToTable("Frames");
+
+                            b1.WithOwner()
+                                .HasForeignKey("FrameId");
+                        });
+
+                    b.Navigation("FirstRoll")
+                        .IsRequired();
+
+                    b.Navigation("PlayerGame");
+
+                    b.Navigation("SecondRoll");
+                });
+
+            modelBuilder.Entity("BowlingTrackerSupreme.Domain.Models.Game", b =>
+                {
+                    b.HasOne("BowlingTrackerSupreme.Domain.Models.Player", "WinningPlayer")
+                        .WithMany()
+                        .HasForeignKey("WinningPlayerId")
+                        .OnDelete(DeleteBehavior.Cascade)
+                        .IsRequired();
+
+                    b.Navigation("WinningPlayer");
+                });
+
+            modelBuilder.Entity("BowlingTrackerSupreme.Domain.Models.PlayerGame", b =>
+                {
+                    b.HasOne("BowlingTrackerSupreme.Domain.Models.Game", "Game")
+                        .WithMany("PlayerGames")
+                        .HasForeignKey("GameId")
+                        .OnDelete(DeleteBehavior.Cascade)
+                        .IsRequired();
+
+                    b.HasOne("BowlingTrackerSupreme.Domain.Models.Player", "Player")
+                        .WithMany("PlayedGames")
+                        .HasFore
```
_Chunk 3_
```
ignKey("PlayerId")
+                        .OnDelete(DeleteBehavior.Cascade)
+                        .IsRequired();
+
+                    b.Navigation("Game");
+
+                    b.Navigation("Player");
+                });
+
+            modelBuilder.Entity("GamePlayer", b =>
+                {
+                    b.HasOne("BowlingTrackerSupreme.Domain.Models.Game", null)
+                        .WithMany()
+                        .HasForeignKey("GameParticipationId")
+                        .OnDelete(DeleteBehavior.Cascade)
+                        .IsRequired();
+
+                    b.HasOne("BowlingTrackerSupreme.Domain.Models.Player", null)
+                        .WithMany()
+                        .HasForeignKey("ParticipantsId")
+                        .OnDelete(DeleteBehavior.Cascade)
+                        .IsRequired();
+                });
+
+            modelBuilder.Entity("BowlingTrackerSupreme.Domain.Models.FinalFrame", b =>
+                {
+                    b.OwnsOne("BowlingTrackerSupreme.Domain.Models.Roll", "ThirdRoll", b1 =>
+                        {
+                            b1.Property<Guid>("FinalFrameId")
+                                .HasColumnType("uuid");
+
+                            b1.Property<int>("PinsHit")
+                                .HasColumnType("integer");
+
+                            b1.HasKey("FinalFrameId");
+
+                            b1.ToTable("Frames");
+
+                            b1.WithOwner()
+                                .HasForeignKey("FinalFrameId");
+                        });
+
+                    b.Navigation("ThirdRoll");
+                });
+
+            modelBuilder.Entity("BowlingTrackerSupreme.Domain.Models.Game", b =>
+                {
+                    b.Navigation("PlayerGames");
+                });
+
+            modelBuilder.Entity("BowlingTrackerSupreme.Domain.Models.Player", b =>
+                {
+                    b.Navigation("PlayedGames");
+                });
+
+            modelBuilder.Entity("BowlingTrackerSupreme.Domain.Models.PlayerGame", b =>
+                {
+                    b.Navigation("Frames");
+                });
+#pragma warning restore 612, 618
+        }
+    }
+}

```

#### File: src/BowlingTrackerSupreme.Migrations/Migrations/20250225212756_AddedCreatedOnModifiedOn.cs
*Summary:* Added CreatedOn and ModifiedOn to entities

**C# format check:**
```
```
**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Migrations/Migrations/20250225212756_AddedCreatedOnModifiedOn.cs b/src/BowlingTrackerSupreme.Migrations/Migrations/20250225212756_AddedCreatedOnModifiedOn.cs
new file mode 100644
index 0000000..c2edcd9
--- /dev/null
+++ b/src/BowlingTrackerSupreme.Migrations/Migrations/20250225212756_AddedCreatedOnModifiedOn.cs
@@ -0,0 +1,128 @@
+﻿using System;
+using Microsoft.EntityFrameworkCore.Migrations;
+
+#nullable disable
+
+namespace BowlingTrackerSupreme.Migrations.Migrations
+{
+    /// <inheritdoc />
+    public partial class AddedCreatedOnModifiedOn : Migration
+    {
+        /// <inheritdoc />
+        protected override void Up(MigrationBuilder migrationBuilder)
+        {
+            migrationBuilder.DropColumn(
+                name: "DateCreated",
+                table: "Games");
+
+            migrationBuilder.RenameColumn(
+                name: "DatePlayed",
+                table: "Games",
+                newName: "PlayedOn");
+
+            migrationBuilder.AddColumn<DateTime>(
+                name: "CreatedOn",
+                table: "Players",
+                type: "timestamp with time zone",
+                nullable: false,
+                defaultValueSql: "timezone('utc', now())");
+
+            migrationBuilder.AddColumn<DateTime>(
+                name: "ModifiedOn",
+                table: "Players",
+                type: "timestamp with time zone",
+                nullable: false,
+                defaultValueSql: "timezone('utc', now())");
+
+            migrationBuilder.AddColumn<DateTime>(
+                name: "CreatedOn",
+                table: "PlayerGames",
+                type: "timestamp with time zone",
+                nullable: false,
+                defaultValueSql: "timezone('utc', now())");
+
+            migrationBuilder.AddColumn<DateTime>(
+                name: "ModifiedOn",
+                table: "PlayerGames",
+                type: "timestamp with time zone",
+                nullable: false,
+                defaultValueSql: "timezone('utc', now())");
+
+            migrationBuilder.AddColumn<DateTime>(
+                name: "CreatedOn",
+                table: "Games",
+                type: "timestamp with time zone",
+                nullable: false,
+                defaultValueSql: "timezone('utc', now())");
+
+            migrationBuilder.AddColumn<DateTime>(
+                name: "ModifiedOn",
+                table: "Games",
+                type: "timestamp with time zone",
+                nullable: false,
+                defaultValueSql: "timezone('utc', now())");
+
+            migrationBuilder.AddColumn<DateTime>(
+                name: "CreatedOn",
+                table: "Frames",
+                type: "timestamp with time zone",
+                nullable: false,
+                defaultValueSql: "timezone('utc', now())");
+
+            migrationBuilder.AddColumn<DateTime>(
+                name: "ModifiedOn",
+                table: "Frames",
+                type: "timestamp with time zone",
+                nullable: false,
+                defaultValueSql: "timezone('utc', now())");
+        }
+
+        /// <inheritdoc />
+        protected override void Down(MigrationBuilder migrationBuilder)
+        {
+            migrationBuilder.DropColumn(
+                name: "CreatedOn",
+                table: "Players");
+
+            migrationBuilder.DropColumn(
+                name: "ModifiedOn",
+                table: "Players");
+
+            migrationBuilder.DropColumn(
+                name: "CreatedOn",
+                table: "PlayerGames");
+
+            migrationBuilder.DropColumn(
+                name: "ModifiedOn",
+                table: "PlayerGames");
+
+            migrationBuilder.DropColumn(
+                name: "CreatedOn",
+                table: "Games");
+
+            migrationBuilder.DropColumn(
+                name: "ModifiedOn",
+                table: "Games");
+
+            migrationBuilder.DropColumn(
+                name: "CreatedOn",
+                table: "Frames");
+
+            migrationBuilder.DropColumn(
+                name: "ModifiedOn",
+                table: "Frames");
+
+            migrationBuilder.RenameColumn(
+                name: "PlayedOn",
+                table: "Games",
+                newName: "DatePlayed");
+
+            migrationBuilder.AddColumn<DateTime>(
+                name: "DateCreated",
+                table: "Games",
+                type: "timestamp with time zone",
+                nullable: false,
+                defaultValue: new DateTime(1, 1, 1, 0, 0, 0, 0, DateTimeKind.Unspecified));
+        }
+    }
+}

```

#### File: src/BowlingTrackerSupreme.Migrations/Migrations/BowlingTrackerSupremeDbContextModelSnapshot.cs
*Summary:* Added CreatedOn and ModifiedOn to entities

**C# format check:**
```
```
**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.Migrations/Migrations/BowlingTrackerSupremeDbContextModelSnapshot.cs b/src/BowlingTrackerSupreme.Migrations/Migrations/BowlingTrackerSupremeDbContextModelSnapshot.cs
index 32bca9c..fea4444 100644
--- a/src/BowlingTrackerSupreme.Migrations/Migrations/BowlingTrackerSupremeDbContextModelSnapshot.cs
+++ b/src/BowlingTrackerSupreme.Migrations/Migrations/BowlingTrackerSupremeDbContextModelSnapshot.cs
@@ -28,6 +28,11 @@ namespace BowlingTrackerSupreme.Migrations.Migrations
                         .ValueGeneratedOnAdd()
                         .HasColumnType("uuid");
 
+                    b.Property<DateTime>("CreatedOn")
+                        .ValueGeneratedOnAdd()
+                        .HasColumnType("timestamp with time zone")
+                        .HasDefaultValueSql("timezone('utc', now())");
+
                     b.Property<string>("Discriminator")
                         .IsRequired()
                         .HasMaxLength(13)
@@ -39,6 +44,11 @@ namespace BowlingTrackerSupreme.Migrations.Migrations
                     b.Property<int>("FrameNumber")
                         .HasColumnType("integer");
 
+                    b.Property<DateTime>("ModifiedOn")
+                        .ValueGeneratedOnAddOrUpdate()
+                        .HasColumnType("timestamp with time zone")
+                        .HasDefaultValueSql("timezone('utc', now())");
+
                     b.Property<Guid>("PlayerGameId")
                         .HasColumnType("uuid");
 
@@ -65,10 +75,17 @@ namespace BowlingTrackerSupreme.Migrations.Migrations
                         .ValueGeneratedOnAdd()
                         .HasColumnType("uuid");
 
-                    b.Property<DateTime>("DateCreated")
-                        .HasColumnType("timestamp with time zone");
+                    b.Property<DateTime>("CreatedOn")
+                        .ValueGeneratedOnAdd()
+                        .HasColumnType("timestamp with time zone")
+                        .HasDefaultValueSql("timezone('utc', now())");
+
+                    b.Property<DateTime>("ModifiedOn")
+                        .ValueGeneratedOnAddOrUpdate()
+                        .HasColumnType("timestamp with time zone")
+                        .HasDefaultValueSql("timezone('utc', now())");
 
-                    b.Property<DateTime>("DatePlayed")
+                    b.Property<DateTime>("PlayedOn")
                         .HasColumnType("timestamp with time zone");
 
                     b.Property<Guid>("WinningPlayerId")
@@ -87,6 +104,16 @@ namespace BowlingTrackerSupreme.Migrations.Migrations
                         .ValueGeneratedOnAdd()
                         .HasColumnType("uuid");
 
+                    b.Property<DateTime>("CreatedOn")
+                        .ValueGeneratedOnAdd()
+                        .HasColumnType("timestamp with time zone")
+                        .HasDefaultValueSql("timezone('utc', now())");
+
+                    b.Property<DateTime>("ModifiedOn")
+                        .ValueGeneratedOnAddOrUpdate()
+                        .HasColumnType("timestamp with time zone")
+                        .HasDefaultValueSql("timezone('utc', now())");
+
                     b.Property<string>("Name")
                         .IsRequired()
                         .HasColumnType("text");
@@ -102,9 +129,19 @@ namespace BowlingTrackerSupreme.Migrations.Migrations
                         .ValueGeneratedOnAdd()
                         .HasColumnType("uuid");
 
+                    b.Property<DateTime>("CreatedOn")
+                        .ValueGeneratedOnAdd()
+                        .HasColumnType("timestamp with time zone")
+                        .HasDefaultValueSql("timezone('utc', now())");
+
                     b.Property<Guid>("GameId")
                         .HasColumnType("uuid");
 
+                    b.Property<DateTime>("ModifiedOn")
+                        .ValueGeneratedOnAddOrUpdate()
+                        .HasColumnType("timestamp with time zone")
+                        .HasDefaultValueSql("timezone('utc', now())");
+
                     b.Property<Guid>("PlayerId")
                         .HasColumnType("uuid");
 

```

#### File: src/BowlingTrackerSupreme.sln
*Summary:* Added player list page

**Raw Diff (chunked):**
_Chunk 1_
```
diff --git a/src/BowlingTrackerSupreme.sln b/src/BowlingTrackerSupreme.sln
index 55be199..e507d4d 100644
--- a/src/BowlingTrackerSupreme.sln
+++ b/src/BowlingTrackerSupreme.sln
@@ -1,7 +1,7 @@
 ﻿
 Microsoft Visual Studio Solution File, Format Version 12.00
 # Visual Studio Version 17
-VisualStudioVersion = 17.13.35806.99 d17.13
+VisualStudioVersion = 17.13.35806.99
 MinimumVisualStudioVersion = 10.0.40219.1
 Project("{2150E333-8FDC-42A3-9474-1A3956D46DE8}") = "Solution Items", "Solution Items", "{9DB2951B-C7D3-4BFB-B9A8-19A80FDA80E6}"
 	ProjectSection(SolutionItems) = preProject
@@ -49,4 +49,7 @@ Global
 	GlobalSection(SolutionProperties) = preSolution
 		HideSolutionNode = FALSE
 	EndGlobalSection
+	GlobalSection(ExtensibilityGlobals) = postSolution
+		SolutionGuid = {1363E8CC-A61A-4008-9BFF-A780BC2C7931}
+	EndGlobalSection
 EndGlobal

```

