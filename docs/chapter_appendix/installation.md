# Installation

## Install IDE

For your local Integrated Development Environment (IDE), we suggest using Visual Studio Code (VS Code) - a lightweight, open-source editor. Head to the [VS Code official website](https://code.visualstudio.com/) to download and install the version that matches your operating system.

VS Code features a robust marketplace of extensions that enables coding and debugging in virtually any programming language. Take Python for example - by installing the "Python Extension Pack", you gain full debugging capabilities for Python code. The figure below demonstrates how to install extensions.

### Github Copilot

We recommend using the AI assistant Github Copilot or other similar tools.
If you are a student, you can apply for a free license of Github Copilot [here](https://github.com/features/copilot).

To install Github Copilot in VS Code, you can search for `Github Copilot` in the VS Code extension marketplace and install it.
Alternatively, you can refer to the [official tutorial](https://docs.github.com/en/copilot/quickstart).

## Cursor

Cursor is a new generation AI-powered IDE that can help you write code faster and more efficiently. 
You can download Cursor from the [official website](https://www.cursor.sh/) and install it. 

## Install language environments

### Python environment

1. Install [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) (Python 3.10+ required) by downloading and running the installer.
2. Open VS Code, go to the Extensions marketplace, search for `python`, and install the Python Extension Pack.
3. (Optional) Install the Black code formatter by running `pip install black` in your terminal.

### R/RStudio environment

1. Download and install [R](https://cran.r-project.org/).
2. In the VS Code extension marketplace, search for `R` and install the R Extension Pack.
3. (Optional but recommended) Install additional packages for enhanced experience:
   - Install `radian` for a modern R console with syntax highlighting and auto-completion
   - Install `httpgd` package for interactive plot viewing
4. More details can be found in the [official tutorial](https://code.visualstudio.com/docs/languages/r).

### C/C++ environment

1. Windows systems need to install [MinGW](https://sourceforge.net/projects/mingw-w64/files/) ([Configuration tutorial](https://blog.csdn.net/qq_33698226/article/details/129031241)); MacOS comes with Clang, so no installation is necessary.
2. In the VS Code extension marketplace, search for `c++` and install the C/C++ Extension Pack.
3. (Optional) Open the Settings page, search for the `Clang_format_fallback Style` code formatting option, and set it to `{ BasedOnStyle: Microsoft, BreakBeforeBraces: Attach }`.

### Java environment

1. Download and install [OpenJDK](https://jdk.java.net/18/) (version must be > JDK 9).
2. In the VS Code extension marketplace, search for `java` and install the Extension Pack for Java.
<!-- 
### C# environment

1. Download and install [.Net 8.0](https://dotnet.microsoft.com/en-us/download).
2. In the VS Code extension marketplace, search for `C# Dev Kit` and install the C# Dev Kit ([Configuration tutorial](https://code.visualstudio.com/docs/csharp/get-started)).
3. You can also use Visual Studio ([Installation tutorial](https://learn.microsoft.com/zh-cn/visualstudio/install/install-visual-studio?view=vs-2022)).

### Go environment

1. Download and install [go](https://go.dev/dl/).
2. In the VS Code extension marketplace, search for `go` and install Go.
3. Press `Ctrl + Shift + P` to call up the command bar, enter go, choose `Go: Install/Update Tools`, select all and install.

### Swift environment

1. Download and install [Swift](https://www.swift.org/download/).
2. In the VS Code extension marketplace, search for `swift` and install [Swift for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=sswg.swift-lang).

### JavaScript environment

1. Download and install [Node.js](https://nodejs.org/en/).
2. (Optional) In the VS Code extension marketplace, search for `Prettier` and install the code formatting tool.

### TypeScript environment

1. Follow the same installation steps as the JavaScript environment.
2. Install [TypeScript Execute (tsx)](https://github.com/privatenumber/tsx?tab=readme-ov-file#global-installation).
3. In the VS Code extension marketplace, search for `typescript` and install [Pretty TypeScript Errors](https://marketplace.visualstudio.com/items?itemName=yoavbls.pretty-ts-errors).

### Dart environment

1. Download and install [Dart](https://dart.dev/get-dart).
2. In the VS Code extension marketplace, search for `dart` and install [Dart](https://marketplace.visualstudio.com/items?itemName=Dart-Code.dart-code).

### Rust environment

1. Download and install [Rust](https://www.rust-lang.org/tools/install).
2. In the VS Code extension marketplace, search for `rust` and install [rust-analyzer](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer). -->
