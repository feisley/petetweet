// ActionScript file
package com.petetweet.client.events
{
	import flash.events.Event;

	public class LoginFailEvent extends Event
	{
		public function LoginFailEvent(bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super("LoginFailEvent", bubbles, cancelable);
		}
		
		override public function clone():Event {
			return new LoginFailEvent();
		}
		
	}
}