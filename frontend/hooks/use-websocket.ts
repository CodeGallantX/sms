import { useEffect, useRef } from 'react';

export const useWebSocket = (url: string, onMessage: (data: any) => void) => {
  const socketRef = useRef<WebSocket | null>(null);

  useEffect(() => {
    const socket = new WebSocket(url);
    socketRef.current = socket;

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      onMessage(data);
    };

    return () => {
      socket.close();
    };
  }, [url, onMessage]);

  const sendMessage = (message: any) => {
    if (socketRef.current && socketRef.current.readyState === WebSocket.OPEN) {
      socketRef.current.send(JSON.stringify(message));
    }
  };

  return { sendMessage };
};
