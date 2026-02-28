"use client";

import { Inter } from "next/font/google";
import "./globals.css";
import { ThemeProvider } from "@/themes/theme-provider";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { useState } from "react";

const inter = Inter({ subsets: ["latin"] });

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const [queryClient] = useState(() => new QueryClient());

  return (
    <html lang="en">
      <body className={inter.className}>
        <QueryClientProvider client={queryClient}>
          <ThemeProvider>
            {children}
          </ThemeProvider>
        </QueryClientProvider>
      </body>
    </html>
  );
}
