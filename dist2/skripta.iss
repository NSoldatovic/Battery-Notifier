; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Battery Notifier"
#define MyAppVersion "2.0"
#define MyAppPublisher "Najjacee"
#define MyAppURL "https://www.ide_gas.com/"
#define MyAppExeName "Battery Notifier.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{08FE287F-1DEF-42A7-BBE0-9BCF3DA12261}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
LicenseFile=D:\Programming\AplikacijeZaUpotrebu\BN\dist2\Licenca.txt
InfoBeforeFile=D:\Programming\AplikacijeZaUpotrebu\BN\dist2\Pre.txt
InfoAfterFile=D:\Programming\AplikacijeZaUpotrebu\BN\dist2\Post.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
PrivilegesRequired=lowest
OutputBaseFilename=BNsetup
SetupIconFile=D:\Programming\AplikacijeZaUpotrebu\BN\dist2\icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\Programming\AplikacijeZaUpotrebu\BN\dist2\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Programming\AplikacijeZaUpotrebu\BN\dist2\config.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Programming\AplikacijeZaUpotrebu\BN\dist2\icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Programming\AplikacijeZaUpotrebu\BN\dist2\ikonica.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Programming\AplikacijeZaUpotrebu\BN\dist2\max_icon.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Programming\AplikacijeZaUpotrebu\BN\dist2\min_icon.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Programming\AplikacijeZaUpotrebu\BN\dist2\options.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Programming\AplikacijeZaUpotrebu\BN\dist2\zvuk.wav"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userstartup}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

