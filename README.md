# Engineering Transformation Case Study — sample repo

This is a focused, reproducible candidate exercise implementation. The included CSV fixtures are **synthetic** and contain no copied names, emails, or raw rows from the supplied workbook. The workbook was inspected to inform data-model and caveat choices; do not publish source data without authorization.

## Prerequisites and run
- .NET 8 SDK for app/workflow
- Python 3.10+ for the data-quality checks

```bash
dotnet run --project src/SampleConsoleApp/SampleConsoleApp.csproj
# In a second terminal:
dotnet test SampleSubmission.sln
python scripts/dora_quality.py
```

## Architecture / contents
- `src/` simple .NET 8 console app with unit-testable service layer.
- `tests/` xUnit tests.
- `.github/workflows/pr-validation.yml` PR build, tests, coverage collection, least-privilege token permissions, and artifact upload.
- `.github/actions/` composite action establishing a reusable platform pattern.
- `data/synthetic/` clearly labelled fixtures for repeatable demo.
- `scripts/dora_quality.py` three executable quality gates.
- `fabric/notebooks/` PySpark medallion implementation sketch for Fabric Lakehouse.
- `docs/` strategy, recommendation, and 5-slide executive presentation.

## Pipeline conversion notes
The supplied Azure YAML installs an x86 SDK/runtime, VC++ redistributable, NuGet, builds an x86 solution using VSBuild, stages output, then runs VSTest with coverage. The GitHub workflow intentionally targets a modern SDK-style .NET 8 solution on Ubuntu x64. If any actual project has x86/native/VS-specific dependencies, use a dedicated Windows runner and explicit architecture-specific validation; do not silently assume equivalence. This sample workflow builds/tests and retains Cobertura XML; it does not publish a deployable release package.

## Fabric review
The notebook is a portable PySpark starting point, not an imported Fabric workspace artifact. Create a Fabric Lakehouse, place authorized source extracts in Bronze, adapt table paths, run Bronze→Silver→Gold, and build a Power BI report over `gold_dora_service_week`. Workspace deployment, credentials, semantic model, dashboard screenshots, and live Fabric execution are not represented here.
