"use client";

import React, { createContext, useContext, useEffect, useState } from 'react';

interface ThemeConfig {
  primary: string;
  secondary: string;
}

const ThemeContext = createContext<ThemeConfig | null>(null);

export const ThemeProvider = ({ children }: { children: React.ReactNode }) => {
  const [config, setConfig] = useState<ThemeConfig>({
    primary: '#3b82f6', // Default blue
    secondary: '#1e293b',
  });

  useEffect(() => {
    // In a real app, fetch theme from API based on subdomain
    const root = document.documentElement;
    root.style.setProperty('--primary', config.primary);
    root.style.setProperty('--secondary', config.secondary);
  }, [config]);

  return (
    <ThemeContext.Provider value={config}>
      {children}
    </ThemeContext.Provider>
  );
};
