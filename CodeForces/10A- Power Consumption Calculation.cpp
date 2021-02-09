#include<bits/stdc++.h>
using namespace std;
int n,p1,p2,p3,t1,t2;
int l,r,s,ans=0;
void inp();
void io();
int main()
{
	inp();
	io();
	return 0;
}
void inp()
{
	cin>>n>>p1>>p2>>p3>>t1>>t2;//Read
}
void io()//Code core
{
	for(int i=1; i<=n; i++)
	{
		cin>>l>>r;
		if(i>1)
		{
			ans=ans+min(t1,l-s)*p1;
			if(l-s>t1)
			{
				ans=ans+min(l-s-t1,t2)*p2;
				if(l-s>t1+t2)
				{
					ans=ans+(l-s-t1-t2)*p3;
				}
			}
		}
		ans=ans+(r-l)*p1;
		s=r;
	}
	cout<<ans;
}
