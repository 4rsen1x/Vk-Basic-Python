words = input().split()
print((lambda s: s[:-1] if len(s)>1 and s[-1]=='0' and s[-2]!='.' else s)(f"{sum(len(w) for w in words)/len(words):.2f}") if words else '0.0')
