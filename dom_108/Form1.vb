Option Explicit Off
Public Class Form1
    Dim g As New ArrayList
    Private Sub Form1_Load(sender As System.Object, e As System.EventArgs) Handles MyBase.Load
        FileOpen(2, "out.txt", OpenMode.Output)
        For ziz = 1 To 2
            FileOpen(1, "in" & ziz & ".txt", OpenMode.Input)
            Do Until EOF(1)
                For z = 1 To Val(LineInput(1))
                    a = LineInput(1).Split({" "}, StringSplitOptions.RemoveEmptyEntries)
                    a1 = Val(a(0))
                    a2 = Val(a(1))
                    s = 0
                    While s <= 50
                        g.Add(a1 \ a2)
                        a1 = a1 Mod a2
                        s += 1
                        If a1 = 0 Then Exit While
                        a1 = a1 & "0"
                    End While

                    If g.Count - 1 <> 50 Then
                        ans = ""
                        For i = 0 To g.Count - 1
                            If i = 1 Then ans &= "."
                            ans &= g(i)
                        Next
                        ans &= "(0)"
                    Else
                        ans = ""
                        q = 0
                        For ii = 1 To 25
                            For i = 1 To g.Count - 2 - ii - ii
                                q1 = ""
                                q2 = ""
                                For j = i To i + ii
                                    q1 &= g(j)
                                Next
                                For j = i + ii + 1 To i + ii + 1 + ii
                                    q2 &= g(j)
                                Next
                                If q1 = q2 Then
                                    ans = q1
                                    q = i
                                    Exit For
                                End If
                            Next
                            If q <> 0 Then Exit For
                        Next
                        If q <> 0 Then
                            If Len(ans) = 2 Then
                                If Mid(ans, 1, 1) = Mid(ans, 2, 1) Then ans = Mid(ans, 1, 1)
                            End If
                            ans1 = g(0) & "."
                            For i = 1 To q - 1
                                ans1 &= g(i)
                            Next
                            ans = ans1 & "(" & ans & ")"
                        Else
                            ans = ""
                            For i = 0 To g.Count - 1
                                If i = 1 Then ans &= ".("
                                ans &= g(i)
                            Next
                            ans &= "...)"
                        End If
                    End If
                    PrintLine(2, Trim(ans))
                    g.Clear()
                Next
            Loop
            FileClose(1)
            If ziz = 1 Then PrintLine(2, "")
        Next
        Close()
        End
    End Sub
End Class
