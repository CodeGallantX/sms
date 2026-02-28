import { create } from 'zustand';

interface TenantState {
  tenant: {
    name: string;
    logo: string;
    primaryColor: string;
    secondaryColor: string;
  } | null;
  setTenant: (tenant: any) => void;
}

export const useTenantStore = create<TenantState>((set) => ({
  tenant: null,
  setTenant: (tenant) => set({ tenant }),
}));
