"use client";

import { useAuthStore } from "@/store/auth-store";
import { useRouter } from "next/navigation";
import { useEffect } from "react";

interface RoleGuardProps {
  children: React.ReactNode;
  allowedRoles: string[];
}

export const RoleGuard = ({ children, allowedRoles }: RoleGuardProps) => {
  const { user } = useAuthStore();
  const router = useRouter();

  useEffect(() => {
    if (user && !allowedRoles.includes(user.role)) {
      router.push("/403");
    }
  }, [user, allowedRoles, router]);

  if (!user || !allowedRoles.includes(user.role)) {
    return null;
  }

  return <>{children}</>;
};
