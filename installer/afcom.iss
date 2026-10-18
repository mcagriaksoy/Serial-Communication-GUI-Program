; Inno Setup script for AFCOM Client.
;
; Produces a per-user Windows installer (no admin rights required): installs
; into %LocalAppData%\Programs\AFCOM Client, creates Start Menu shortcuts and
; an optional desktop shortcut, and allows a clean uninstall.
;
; The CI workflow builds the portable executable first, then compiles this
; script, passing the version, source executable and output directory:
;
;   ISCC.exe /DVersion=1.9.0 /DSourceExe=<abs path> /DOutputDir=<abs path> afcom.iss
;
; The defaults below allow compiling locally from the repository as well.

#ifndef Version
  #define Version "0.0.0"
#endif

#ifndef SourceExe
  #define SourceExe "..\dist\AFCOM_v" + Version + "_portable_win64.exe"
#endif

#ifndef OutputDir
  #define OutputDir "..\dist"
#endif

[Setup]
AppId={{9B1E7F42-3C6A-4D58-A2F1-7E4C0B8D5A31}
AppName=AFCOM Client
AppVersion={#Version}
AppVerName=AFCOM Client {#Version}
AppPublisher=Mehmet Cagri Aksoy
AppPublisherURL=https://github.com/mcagriaksoy/Serial-Communication-GUI-Program
AppSupportURL=https://github.com/mcagriaksoy/Serial-Communication-GUI-Program
AppUpdatesURL=https://github.com/mcagriaksoy/Serial-Communication-GUI-Program/releases
DefaultDirName={localappdata}\Programs\AFCOM Client
DefaultGroupName=AFCOM Client
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
OutputDir={#OutputDir}
OutputBaseFilename=AFCOM_Client_v{#Version}_win64_setup
SetupIconFile=..\ui\icon.ico
UninstallDisplayIcon={app}\AFCOM.exe
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
LicenseFile=..\LICENSE

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "turkish"; MessagesFile: "compiler:Languages\Turkish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "{#SourceExe}"; DestDir: "{app}"; DestName: "AFCOM.exe"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\AFCOM Client"; Filename: "{app}\AFCOM.exe"
Name: "{autodesktop}\AFCOM Client"; Filename: "{app}\AFCOM.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\AFCOM.exe"; Description: "{cm:LaunchProgram,AFCOM Client}"; Flags: nowait postinstall skipifsilent
