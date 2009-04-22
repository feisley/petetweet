// ActionScript file
package com.petetweet.client.events
{
	import flash.events.Event;

	public class LoginFailEvent extends Event
	{
		public function LoginFailEvent(error:Object, bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super("LoginFailEvent", bubbles, cancelable);
			
			this.error = error;
		}
		
		public var error:Object;
		
		override public function clone():Event {
			return new LoginFailEvent(error);
		}
		
	}
}