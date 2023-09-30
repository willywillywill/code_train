Public Class p41

    Private Sub p41_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        FileOpen(1, "in1.txt", OpenMode.Input)
        FileOpen(2, "in2.txt", OpenMode.Input)
        FileOpen(3, "out.txt", OpenMode.Output)
        For file = 1 To 2
            Dim b = LineInput(file)
            For i = 1 To Val(b)
                Dim a() As String = LineInput(file).Split({"[", ",", "]"}, StringSplitOptions.RemoveEmptyEntries)
                Dim n As Integer = a.Length
                Dim s As New ArrayList
                Dim j = 0
                Dim g = 0
                Dim k = 0
                g = ff(1, a.Length - 1, a, 0)
                Dim kk = 0
                g = g + f(2, a.Length - 1, a, 0)
                PrintLine(3, g)
            Next
            PrintLine(3)
        Next
        Me.Close()
    End Sub
    Function f(ByVal x, ByVal max, ByVal a(), ByRef kk)
        If x > max Then Return kk
        If a(x) = "null" Then
            Return f(x - 1, max, a, kk)
        Else
            Return f(x * 2 + 2, max, a, kk + 1)
        End If
    End Function
    Function ff(ByVal x, ByVal max, ByVal a(), ByRef kk)
        If x > max Then Return kk
        If a(x) = "null" Then
            Return f(x + 1, max, a, kk)
        Else
            Return f(x * 2 + 1, max, a, kk + 1)
        End If
    End Function
End Class
