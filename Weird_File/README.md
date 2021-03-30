# Weird File

Category: Forensics </br>
AUTHOR: THELSHELL

**Disclaimer! I do not own the challenge files!**

## Description
```
What could go wrong if we let Word documents run programs? (aka "in-the-clear").
```

## Word document

After clicking the link a Word document `weird.docm` is downloaded. Now a little known fact (for some), almost everything that is MS proprietary is just XML and zip (some of you might be pulling your hair, but hey... I think the description works). So what could we do with this? Sure, you could just run `file`, `binwalk` and `strings`. Or! Just use 7z (you can even download it for WIndows). 

```
$ 7z x weird.docm
```
*On windows just right-click, navigate to 7z and extract*
</br></br>

So what did we extract?
```
$ ls
'[Content_Types].xml'   customXml   docProps   _rels   weird.docm   word
```
Great! 

## Finding the weird stuff

In word, powerpoint and other documents you can use macros. This allows evil leet h4x0rs to embed code in your word document that will execute (unless you have macros switched off, which you should!). Maybe this is the case here as well? 
```
$ ls *
'[Content_Types].xml'   weird.docm

customXml:
item1.xml  itemProps1.xml  _rels

docProps:
app.xml  core.xml

_rels:

word:
document.xml  fontTable.xml  _rels  settings.xml  styles.xml  theme  vbaData.xml  vbaProject.bin  webSettings.xml
```
`vbaProject.bin` and `vbaData.xml`? That shouldn't be there, I don't think. Maybe there is something in there?
```
$ strings vbaProject.bin 
%RL9
Macros can run any program
Title
world!
some text
llow 
Couldn't run python script!
Ret_Val = Shell("python -c 'print(\"cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9\")'" & " " & Args, vbNormalFocus)
Attribut
e VB_Nam
e = "Thi
sDocumen
1Normal.
...
...
...
```
Oh, great. I don't think Word ships with this. But that string is definitely `base64`:

### Flag on linux
```bash
echo cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9 | base64 -d
picoCTF{m4cr0s_r_d4ng3r0us}
```
Indeed they are Pico.

### Flag on Windows (powershell)
```powershell
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9'))
picoCTF{m4cr0s_r_d4ng3r0us}
```