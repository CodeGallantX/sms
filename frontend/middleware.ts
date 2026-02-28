import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const url = request.nextUrl.clone();
  const hostname = request.headers.get('host') || '';

  // Exclude internal Next.js paths and static files
  if (
    url.pathname.startsWith('/_next') ||
    url.pathname.includes('.')
  ) {
    return NextResponse.next();
  }

  const subdomain = hostname.split('.')[0];
  const isLocal = hostname.includes('localhost');
  const isMainDomain = subdomain === 'www' || (isLocal && subdomain === 'localhost');

  // Handle subdomain routing logic here if needed
  // For now, we just pass through and let the client-side handle tenant context

  return NextResponse.next();
}

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
};
